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

from ..Editor.Cath_Editor_Extras import update_text_info, write_area, key_home
from ..Editor.Cath_Editor_Select import cut
from ..Editor.SHARED             import clear_selected

# Enter Key
def enter(self):

    write_area(self)
    # If text file lines are less than length of maximum displayable lines
    # Add an extra line to textfile displayable line limit
    if self.total_lines < (self.max_lines - 1):
        self.total_lines += 1
    
    # If cursor at end of line
    if self.pos == len(self.current_text):
        
        self.chars = 0
        self.pos   = 0
        self.lines.insert(self.i + 1, "")                 # Insert blank line into list/ file
        
    # If cursor is NOT at end of line
    elif self.pos != len(self.current_text):
        self.lines[self.i] = self.before                          # Get text of line that is before cursor
        self.lines.insert(self.i+1, self.after)                   # Insert all text after cursor on a new line to file list
        self.pos   = 0                                            # Reset cursor to line beginning
        
        # Current displayed Line is the bottom, remove top line from screen
    if self.display_current_line < self.total_lines:
        self.display_current_line += 1
        
    self.current_line += 1
    update_text_info(self)
    self.enter         = 1
        
    # Bring cursor and screen to satrt of line
    key_home(self)
 
def add_space(self, what):
    
    update_text_info(self)
    
    if what == "space":
        what   = " "
        amount = 1

    elif what == "tab":
        what   = "    "
        amount = 4
        
    elif what == "enter":
        what   = ""
        amount = 0

    write_area(self)
            
    if self.selected == 1:
        
        cut(self, self.start, self.end)
        self.pos += 1
        update_text_info(self)
        self.current_text                      = self.before + what + self.after
        self.lines[self.i]                     = self.current_text
        self.pos += amount
        update_text_info(self)
        clear_selected(self)
        
    else:
        # Make adjustment for 'INSERT'
        if self.insert == 0:
            self.current_text = self.before + what + self.after
        else:
            self.current_text = self.before + what + self.after[amount:]
        
        self.lines[self.i]                     = self.current_text
        self.pos += amount
    
    # Do we need to scroll horizontally?
    if self.pos > self.max_line_chars + self.new_pos:
        self.new_pos += amount
        #self.new_pos = self.pos - self.max_line_chars
    
    self.chars = len(self.lines[self.i])
    update_text_info(self)
    self.selected = 0
