#######################################################################################################
#
#    This file is part of CATH || PyGame_GUI Text Editor.
#
#    CATH is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    CATH is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with CATH.  If not, see <https://www.gnu.org/licenses/>.
#
#######################################################################################################

import pygame as P
from ..Editor.SHARED import Col, clear_selected, update_scroll_info
from ..Editor.Cath_Editor_Select import copy_paste, cut, remove
from ..Editor.Cath_Editor_Extras import update_text_info, write_area, clip_nav
from ..Editor.Cath_Editor_Key import key_down
from ..Editor.SQUARE import Square
import time, os


class PyEdit_no_gui:
    
    def __init__(self, X, Y, width, height, FPS, FONT, text_size, font_colour, parent):
        
        print('Loading Backend')
        
        self.CATH              =   self
        self.parent            =   parent
        
        self.width             =   width
        self.height            =   height
        self.FPS               =   FPS
        self.X                 =   X
        self.Y                 =   Y
        
        # Font variables
        self.FONT              =   FONT
        self.text_size         =   text_size
        self.font_colour       =   font_colour
        self.text_width        =   round(self.text_size / 2)
        
        # Cursor
        self.cur_col           =   "grey"
        self.Cdir              =   0      # Set direction of cursor blinking animation
        self.cursor_colour     =   0
        self.search            =   0
        self.cursor_length     =   1
        self.re_search         =   0
        self.selected          =   0
        self.start             =   [0, 0]
        self.end               =   [0, 0]
        self.upwards           =   0
        self.selected_text     =   []
        self.select_cache      =   []
        self.start_point       =   []
        self.end_point         =   []
        
        # Editor variables
        self.real              =   0
        self.save_file         =   0
        self.open_file         =   0
        self.max_line_chars    =   round(self.width / self.text_width) - 2
        self.max_lines         =   round((self.height)/ self.text_size) - 2
        self.rock_bottom       =   0
        self.only_display      =   0
        print("Max Lines:", self.max_lines, "Max Chars:", self.max_line_chars)
        
        # Key Variable
        self.key               =   0
        self.enter             =   0
        self.back_space        =   0
        self.ctrl              =   0
        self.alt               =   0
        self.super             =   0
        self.caps              =   0
        self.Lshift            =   0
        self.Rshift            =   0
        self.insert            =   0
        self.ignore_keys       =   []
        
        # Non alpha-numeric characters
        self.special = [[96, 126],[49, 33],[50, 64],[51, 35],[52, 36],[53, 37],[54, 94],[55, 38],
                        [56, 42],[57, 40],[48, 41],[45, 95],[61, 43],[92, 124], [91, 123], [93, 125],
                        [59,58],[39,34],[44,60],[46,62],[47,63]]
        
        # Modifier keys (SHIFT, ALT, etc)
        self.MODIFIERS = [301, 308, 307, 305, 306, 304, 303, 309, 1073742055]

        # Arrow keys (up, down, right, left)
        self.ARROWS = [273, 274, 275, 276]
        
        # Navigation keys (pg up, pgdown, home, end)
        self.NAVIGATION = [280, 281, 278, 279]
        
        # Writing/ word/ letter variables
        self.lines         =   [""] 
        self.line          =   0
        self.chars         =   0
        self.home          =   1
        self.real          =   0  # Difference between dislayed and real line
        self.no_entry      =   0  # Lets us dis/enable typing
        self.pos_offset    =   0
        self.MAX_chars     =   0 # Maximun file line length constant
        
        # Default file to open on start
        dir_ = os.getcwd()        
        try:
            self.default_file  = dir_ + "/apps/tools/CATH/Editor/temp.txt"
            self._file_        = open(self.default_file, 'r').readlines()
            
            # Read all lines from file into 'self.lines' list
            for line in self._file_:    
                self.lines.append(line.replace("\n", ""))
            self.lines.pop(0)
        except:
            E = Exception
            print(E)
        else:
            # Put only the amount of lines which will be visible into list
            if len(self.lines) > self.max_lines:
                self.total_lines = self.max_lines
            else: self.total_lines = len(self.lines)
                
        print('File Lines =', len(self.lines), 'Total Lines', self.total_lines)
        
        self.lines.append("")
        self.pos                  =   0
        self.new_pos              =   0 # Get difference between cursor pos and length of text if line is greater tha max line length
        self.display_pos          =   0
        self.current_line         =   1
        self.display_current_line =   self.current_line
        self.current_text         =   self.lines[0]
        self.chars                =   len(self.current_text)
        self.current_pos          =   self.pos
        self.before               =   self.current_text[:self.pos]
        self.after                =   self.current_text[self.pos:]
        self.i                    =   self.current_line - 1
        self.current_text         =   self.lines[self.i]
        self.paste                =   []
        
        #General variables
        self.running      =   True
        self.FPS_count    =   0
        self.temp         =   0
        
        P.key.set_repeat(1, 200) # Modify to control speed of cursor when key held dowm
        
        # Define key behaviour
        # Define keys to ignore from displaying any special character formatting
        self.ignore_keys = [127, 8, 9, 13, 27, 32, 277]
        
        for item in self.MODIFIERS:
            self.ignore_keys.append(item)
        for item in self.ARROWS:
            self.ignore_keys.append(item)
        for item in self.NAVIGATION:
            self.ignore_keys.append(item)
            
        self.Clip_board = ""#Square(screen, 0, 0, 0, 0, orient = "vertical",
                            #colour = "grey", fill = True, line_width = 0)
        
    # What happens when a key is released
    def key_up(self, key):
    
        # modifiers release
        if self.no_entry == 0 and key == 305 or key == 306       : self.ctrl  = 0
        if self.no_entry == 0 and key == 307 or key == 308       : self.alt   = 0
        if self.no_entry == 0 and key == 309 or key == 1073742055: self.super = 0
        
        # arrows release
        for item in self.ARROWS:
            if self.no_entry == 0 and key == item: self.arrow = 0
        
        # caps OFF
        if self.no_entry == 0 and key == 301: self.caps = 0
        
        # L and R shift release
        if   key == 303: self.Rshift = 0
        elif self.no_entry == 0 and key == 304: self.Lshift = 0
        
        # Backspace release
        if self.no_entry == 0 and key == 8: self.back_space = 0
        
        # CTRL - V Used for pasting text and Clipboard use
        if key == 118:
            pass
              
    def draw(self, surface):
        
        self.display_pos = self.pos - self.new_pos
        
        def render_body_of_text(self, surface):
        
            font = P.font.Font(self.FONT, self.text_size)
            
            for l in range(self.total_lines):             
                text = self.lines[l + self.real]
                
                if self.new_pos > 0:
                    text = text[self.new_pos:self.max_line_chars + self.new_pos]
                    
                else:
                    text = text[:self.max_line_chars]
       
                Text = font.render(text, True, Col(self.font_colour))
                if self.parent.numbers == 1:
                    surface.blit(Text, (self.parent.EditorX + self.parent.offset, self.Y + (l * self.text_size)))
                else:
                    surface.blit(Text, (self.parent.offset, self.Y + (l * self.text_size)))
        
        # Render Cursor
        def render_cursor(self, surface):
            
            # CURSOR Blinking
            if self.display_current_line > 0 and self.display_current_line <= self.max_lines:
                
                # If not in 'INSERT' mode: do blinking
                if self.insert == 0 and self.search == 0:
                    if self.FPS_count == 0: self.Cdir = (self.Cdir + 1) % 2
                    
                    if self.Cdir == 1: self.FPS_count = (self.FPS_count + 3) % self.FPS
                    else             : self.FPS_count = (self.FPS_count - 3) % self.FPS
                    
                    if self.FPS_count != 0:
                        self.cursor_colour = round((50 / self.FPS) * self.FPS_count)
                else: self.cursor_colour = 45
                    
                if self.caps == 1    : self.cur_col = "red"    # Change colour for CAPS on/ off
                elif self.search == 1:
                    self.cur_col = "red"      # Yellow for search function
                    self.cursor_colour = 75
                else: self.cur_col = "grey"   # Regular cursor colour
                
                # Update cursor screen position
                self.display_pos = self.pos - self.new_pos
                # Offset if displaying line numbers
                if self.parent.numbers == 1:
                    Cx  = 1 + (self.text_width * self.display_pos + 1) + ((self.parent.nums) * self.text_width) + self.parent.offset
                else:
                    Cx  = 1 + (self.text_width * self.display_pos + 1)
                
                Cy  = self.Y + self.text_size + ((self.display_current_line -1) * self.text_size)
                Cy2 = Cy
                
                # Change cursor appearance if in 'INSERT' or 'SEARCH' modes
                if self.insert == 1 or self.search == 1:
                    cW  = self.text_size
                    offset = self.text_size // 2
                    if self.search == 1: Cx2 = Cx + (self.text_width * self.cursor_length)
                    else: Cx2 = Cx + self.text_width
                else:
                    cW = 2
                    offset = 0
                    if self.search == 1: Cx2 = Cx + (self.text_width * self.cursor_length)
                    else: Cx2 = Cx + self.text_width
                    
                # Draw Cursor
                cursor = P.draw.line (surface, Col(self.cur_col, self.cursor_colour),
                                      (Cx, Cy - offset), (Cx2, Cy2 - offset) ,cW)
        
        render_cursor(self, surface)
        render_body_of_text(self, surface)
    
    # Get the difference between the current displayed line and the actual line
    #def get_over(self):
    #    over = self.current_line - self.total_lines
    #    return([over + 1, self.current_line, self.display_current_line])
    
    # Get info about the current cursor position + other stuff
    def get_pos(self):
        # This next statement stops CATH crashing when selecting multiple lines of
        # text from the bottom line upwards....
        #if self.current_line > len(self.lines):
        #    self.current_line > len(self.lines)
        
        pos = [self.pos, self.current_line, len(self.lines[self.current_line - 1]),
               len(self.lines) - 1, self.caps, self.total_lines]
        return(pos)
    
    # Get event input  
    def update(self, event):
        
        # Key Press
        if event.type == P.KEYDOWN:
            if self.save_file == 0 and self.open_file == 0:
                key_down(self, event.key)
        if event.type == P.KEYUP  :
            if self.save_file == 0 and self.open_file == 0:
                self.key_up(event.key)
    
    # Update Maximum display-able Lines. Used when window size changes...
    def update_max_lines(self):
        update_text_info(self)
        # TODO:
        # IF bottom lines appears at bottom stop extending display lines
        # Only grow lines if all lines of file are not on screen
        if len(self.lines) - 1 < self.max_lines:
            self.total_lines = len(self.lines) - 1
        else: self.total_lines = self.max_lines
            
    print('Cath Editor Backend Initialised') 
                
            
            
