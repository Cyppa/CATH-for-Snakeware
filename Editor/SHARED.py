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

from ..Editor.Cath_Editor_Extras import update_text_info
from ..ASSETS.ASSETS_REBUILDER   import build_home_assets

# Take us back to home screen
def go_home(self, ui_manager):
    # Home Screen
    home_hide = [self.numbers_button, self.colours_button, self.save_button, self.cursor_button,
                 self.open_button, self.text_button1, self.grid_slider,
                 self.text_button2, self.quit_button_no_save, self.quit_button_save,
                 self.text_entry_search, self.search_down, self.search_up,
                 self.text_entry_replace, self.replace, self.all, self.new_file_button]
    
    for item in home_hide: item.kill()
        
    build_home_assets(self, ui_manager)
    
    self.home_button.disable()
    self.options_button.enable()
    self.disk_button.enable()
    self.search_button.enable()
    self.quit_button.enable()

# Update line scrolling info when new file is opened
def update_scroll_info(self):
        
    update_text_info(self.CATH)
    
    total_Y             = len(self.CATH.lines)             # Total lines of text in file
    total               = self.CATH.max_lines / total_Y    # How many times do total file lines divide into screen space
    self.parent.V_bar_length   = (self.parent.body_Y - self.parent.EditorY) * total              # Scroll Bar Length
    self.parent.current_line   = self.CATH.current_line
    self.parent.V_scroll_steps = self.surface_size[1] - (self.V_scroll_Y + self.V_bar_length)
    line_dif            = len(self.CATH.lines) - self.CATH.max_lines
    
    self.parent.scroll_TOP = self.V_step
    self.parent.scroll_BOT = self.scroll_TOP + self.V_bar_length
    
    if len(self.CATH.lines) >  self.CATH.max_lines:
        self.parent.move_lines  = self.V_scroll_steps / line_dif
        self.parent.move        = int(self.V_step / self.move_lines)        

# From PyGameGui self.CATH. Save/ Load method...
def save_load(self, option, file_name):
        
    # Saving File
    if option == 'save':
        
        self.CATH.save_file = 1
        print("SAVE FILE", file_name)
        try:
            with open(file_name, 'w') as file_:
        
                for l in range(len(self.CATH.lines) - 1):
                    print(self.CATH.lines[l], file = file_)
            self.parent.top_label.set_text(("FILE SAVED!")[:self.parent.top_label_chars])      
            self.CATH.save_file = 0
        
        except FileNotFoundError:
            self.top_label.set_text(("FILE NEEDS A NAME!")[:self.parent.top_label_chars])
            self.save_error = True
            
    # Loading file
    if option == 'open':
        
        print(file_name)
        self.CATH.open_file = 1
        self.CATH.lines.clear()
        file_open = open(file_name, 'r')
        _file_ = file_open.readlines()
        
        self.CATH.total_lines = self.CATH.max_lines

        for l in range(len(_file_)):
            self.CATH.lines.append(_file_[l].replace("\n", ""))
        
        if len(self.CATH.lines) <= self.CATH.total_lines:
            self.CATH.total_lines = len(self.CATH.lines)
        else:
            self.CATH.total_lines = self.CATH.max_lines
        
        self.CATH.chars                = len(self.CATH.lines[self.CATH.real])
        self.CATH.pos                  = 0
        self.CATH.current_line         = 1
        self.CATH.display_current_line = 1
        self.CATH.open_file            = 0
        self.CATH.lines.append("")
        file_open.close()
        
        #update_scroll_info(self)

# Clear the Text Selection
def clear_selected(self, cursor = 1):
    
    if cursor == 1:
        self.CATH.cX1, self.CATH.cY1   = 0, 0 
        self.CATH.cX2, self.CATH.cY2   = 0, 0
    
    self.CATH.selX1,  self.CATH.selY1  = 0, 0
    self.CATH.selX2,  self.CATH.selY2  = 0, 0
    self.CATH.selX1a, self.CATH.selY1a = 0, 0
    self.CATH.selX2a, self.CATH.selY2a = 0, 0
    self.CATH.bX1,    self.CATH.bY1    = 0, 0
    self.CATH.bX2,    self.CATH.bY2    = 0, 0

# Jump to Line #
def GOTO_line(self, integer, pos = 0):
    
    def do():
        self.CATH.current_line = integer
        self.CATH.pos          = 0
        self.CATH.display_pos  = 0
        update_text_info(self.CATH)
        self.parent.top_label.set_text(("MOVED!")[:self.parent.top_label_chars])
        self.parent.scrolled          = 0
        get_current_over       = self.CATH.current_line - self.CATH.max_lines
        #self.move_bar          = get_current_over * self.move_lines
        #self.scroll_TOP_       = self.scrollY + self.move_bar
        
    if integer < self.CATH.max_lines and integer < len(self.CATH.lines):
        self.CATH.display_current_line = integer
        do()
        
    elif integer < len(self.CATH.lines):
        diff = integer - self.CATH.max_lines
        self.CATH.display_current_line = self.CATH.max_lines
        do()  
    else:
        self.parent.top_label.set_text(("Out Of Range!")[:self.parent.top_label_chars])
        print("Too Far!")

# Colour Selector
# Lets us choose a colour and it's intensity
# '0' is darkest to '100' which is brightest
def Col(col, num = 100):
        
    X = int((255 / 100) * num)
    colour = (0,    0,    0)
    
    if   col ==   "black": colour = (0,    0,    0)
    elif col ==    "grey": colour = (X,    X,    X)
    elif col ==     "red": colour = (X,    0,    0)
    elif col ==   "green": colour = (0,    X,    0)
    elif col ==    "blue": colour = (0,    0,    X)
    elif col ==  "yellow": colour = (X,    X,    0)
    elif col ==    "cyan": colour = (0,    X,    X)
    elif col == "magenta": colour = (X,    0,    X)
    elif col ==   "white": colour = (255, 255, 255)
    
    return(colour)