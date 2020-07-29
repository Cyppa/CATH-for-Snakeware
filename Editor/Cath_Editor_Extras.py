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

### Extra methods for CathEditor.py
import time

from ..Editor.SQUARE import Square

# Bring cursor and screen to character position 0
def key_home(self):
    
    self.display_pos = 0
    self.pos         = 0
    self.new_pos     = 0
    self.update_max_lines()
    update_text_info(self)

# After each key press update certain bits of information
def update_text_info(self):
    
    self.get_pos()
    self.i            =   self.current_line - 1
    self.current_text =   self.lines[self.i]
    self.before       =   self.current_text[:self.pos]
    self.after        =   self.current_text[self.pos:]
    
    self.display_pos = self.pos - self.new_pos
    
    self.chars = len(self.current_text)
    
    if (self.current_line != self.display_current_line):
        self.real = self.current_line - self.display_current_line
    else: self.real = 0
    
    self.search = 0

# Not sure if next method is necesarry anymore?   
def reset(self):
    
    if self.total_lines > len(self.lines):
        self.total_lines = len(self.lines)
    
    if self.total_lines > self.max_lines:
        self.total_lines = self.max_lines
    #unfinished
    else:
        disp = len(self.display_lines)
        diff = self.total_lines - len(self.display_lines)
        
def write_area(self):
    # If text not in displayable are, goto displayable area
    if self.display_current_line < 1 or self.display_current_line > self.max_lines:
            GOTO_line(self, self.current_line, self.pos)
            time.sleep(0.1)

# Navigate Clipboard with up/ down arrows
def clip_nav(self, direction):
            
    if direction == "up": plus = -1
    else: plus = 1
    
    self.cached_list.clear()
    self.cached_line = ""
    length           = len(self.start_end)
    self.cacheX      = (self.cacheX + plus) % length
    
    for r in range(self.start_end[self.cacheX][0],self.start_end[self.cacheX][1] + 1):
        self.cached_list.append(self.cache[r].replace("\n", ""))
    
    for line in self.cached_list:
        if line == "": line = "''"
        self.cached_line = self.cached_line + " '" + line + "'"
    
    Y = ((self.current_line - self.real) * self.text_size) + self.EditorY
    self.Clip_board = Square(self.screen, 50, Y, self.W - 100, int(self.text_size * 1.5), orient = "vertical",
                    colour = "grey", fill = True, line_width = 2)
    self.show_clip = 1
