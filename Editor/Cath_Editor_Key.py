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
from ..Editor.SHARED                 import Col, clear_selected, update_scroll_info, GOTO_line
from ..Editor.Cath_Editor_Select     import copy_paste, cut, remove
from ..Editor.Cath_Editor_Extras     import update_text_info, write_area, clip_nav, key_home
from ..Editor.Cath_Editor_Backspace  import backspace
from ..Editor.Cath_Editor_Delete     import delete
from ..Editor.Cath_Editor_Add_Spaces import add_space, enter
from ..Editor.Cath_Editor_Write      import write

from ..Editor.SQUARE import Square

#What happens when a key is pressed down
def key_down(self, key):

    #print(key)
    self.re_search = 1
    self.text      = ""
    self.enter     = 0
    self.back      = 0
    self.change    = 0
    self.modifier  = 0
    self.arrow     = 0
    self.ignore    = 0
    
    # MODIFIERS
    # L and R shift
    if self.no_entry == 0 and key == 304: self.Lshift = 1
    if self.no_entry == 0 and key == 303: self.Rshift = 1
    
    # Caps ON
    if self.no_entry == 0 and key == 301: self.caps = 1
    
    # CTRL/ ALT/ SUPER
    if (self.no_entry == 0 and key == 305 or key == 306 and self.save_file == 0 and
        self.open_file == 0):
        self.ctrl  = 1
    
    if (self.no_entry == 0 and key == 307 or key == 308 and self.save_file == 0 and
        self.open_file == 0):
        self.alt   = 1
    
    if self.no_entry == 0 and key == 309 or key == 1073742055: self.super = 1
        
    # NAVIGATION and ARROW KEYS
    for item in self.ARROWS:
        if self.no_entry == 0 and key == item: self.arrow = 1
    
    # UP
    if self.no_entry == 0 and key == 273 and self.ctrl == 0:
        
        update_text_info(self)
        self.chars = len(self.lines[self.current_line - 2])
        
        if self.chars < self.current_pos:
            self.pos = self.chars
        else: self.pos = self.current_pos
        
        if self.current_line > 1:
            self.current_line -= 1
        else:
            # We are at top, bring scroll bar to home/ rest
            self.parent.scroll_TOP = self.parent.V_scroll_Y
            
        if self.display_current_line > 1:
            self.display_current_line -= 1
                
        self.parent.selected = 0
        self.parent.selecting = 0
        clear_selected(self)
        key_home(self)
        update_text_info(self)
    
        
    # DOWN
    if self.no_entry == 0 and key == 274 and self.ctrl == 0:
        
        update_text_info(self)
        
        if len(self.lines) - 1 < self.max_lines:
            self.total_lines = len(self.lines) - 1
        else: self.total_lines = self.max_lines
        
        # Update character info of line we move to
        self.chars = len(self.lines[self.current_line])
        
        if self.chars < self.current_pos:
            self.pos = self.chars
        else: self.pos = self.current_pos
        
        if self.current_line < len(self.lines) - 1:
            self.current_line += 1
        else:
            #We are at the lat line of file
            # Bring bar to rest in its bottom home
            self.parent.scroll_TOP = self.parent.surface_size[1] + self.parent.offset + self.parent.V_bar_length
            
        if self.display_current_line < self.total_lines:
            self.display_current_line += 1
            
        self.selected = 0
        self.selecting = 0
        clear_selected(self)
        key_home(self)
        update_text_info(self)

        
    # LEFT
    if self.no_entry == 0 and key == 276:
        
        if self.pos > 0:
            self.pos -= 1
            self.selected      = 0
            self.selected = 0
            clear_selected(self)
            
            # If cursor at start of screen but not at start of line
            if self.display_pos <= 0:
                self.new_pos -= 1
            
            update_text_info(self)
            
    # RIGHT
    if self.no_entry == 0 and key == 275:                    
        
        update_text_info(self)
        if self.pos < self.chars:
            
            self.pos += 1
            self.selected      = 0
            self.selected = 0
            clear_selected(self)
            
            # If cursor at end of screen but not end of current line:
            # For purposes of horizontal scroling
            if self.pos >= self.max_line_chars + self.new_pos:
                self.new_pos += 1
                
            update_text_info(self)
    
    # Page Up
    if self.no_entry == 0 and key == 280:
        # If current line is greater than maximum amount of displayable lines
        if self.current_line > self.max_lines:
            CUR = self.current_line - self.max_lines + 1
        else:
            # Cursor to top line of screen
            CUR = 1
        
        # Position cursor to line and character
        self.current_line         = CUR
        self.display_pos          = 0
        self.pos                  = 0
        self.display_current_line = 1
        
        update_text_info(self)
        key_home(self)
    
    # Page Down
    if self.no_entry == 0 and key == 281:
        
        # If file lines are greater than current line + max displayable lines
        if len(self.lines) > self.current_line + self.max_lines:
            # Move one screen down
            CUR = self.current_line + self.max_lines - 1
        else:
            # Or Just move Cursor to bottom line of screen
            CUR = len(self.lines) - 1
        
        # Position cursor to line and character
        self.current_line         = CUR
        self.display_pos          = 0
        self.pos                  = 0
        self.display_current_line = self.max_lines
        
        update_text_info(self)
        
        key_home(self)
    
    # Home
    if self.no_entry == 0 and key == 278:
        update_text_info(self)
        key_home(self)
    
    # End
    if self.no_entry == 0 and key == 279:
        
        update_text_info(self)
        self.display_pos = self.max_line_chars
        self.pos         = self.chars
        
        # Do we need to scroll text?
        if self.chars > self.max_line_chars:
            self.new_pos = self.chars - self.max_line_chars
        
        update_text_info(self)
        
    # TEXT REMOVAL
    # DEL
    if self.no_entry == 0 and key == 127:
        if self.save_file == 0 and self.open_file == 0:
            delete(self)
    
    # Backspace
    if self.no_entry == 0 and key == 8:
        backspace(self)
    
    #ADDING SPACES      
    # Tab
    if self.no_entry == 0 and key == 9:
        if self.save_file == 0 and self.open_file == 0:                
            add_space(self, "tab")

    # Spacebar
    if self.no_entry == 0 and key == 32:
        if self.save_file == 0 and self.open_file == 0:
            add_space(self, "space")
            
    # Enter
    if self.no_entry == 0 and key == 13:
        
        if self.selected == 1:
            add_space(self, "enter")
        
        enter(self)
    
    # Extra Special Keys
    # ESC
    if self.no_entry == 0 and key == 27:
        pass   
    
    # Insert
    if self.no_entry == 0 and key == 277:
        write_area(self)
        self.insert = (self.insert + 1) % 2

    # Display Character to Screen
    write(self, key)   
                       
    # Remove any specia"l formatting that may inadvertantly arise    
    self.text = self.text.replace('\x08', '').replace('\x1b', '').replace('\x7f', '')

