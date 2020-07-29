####################################################################################
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
####################################################################################
import pygame
from ..Editor.SHARED import Col

def update_Hscroll(self):
# Get length of longest line in file (in characters)
    for line in self.CATH.lines:
        if len(line) > self.longest_line: 
            self.longest_line = len(line)
    
    # Do we need Horizontal bar?
    if self.longest_line > self.CATH.max_line_chars:
        
        self.over_chars   = self.longest_line - self.CATH.max_line_chars   # Difference between longest line and max chars
        total             =  self.CATH.max_line_chars / self.longest_line  # How many times longest line fits into max chars
        self.H_bar_length = (self.surface_size[0] - self.scroll_W) * total # Horizontal Bar length
        scrolling_space   = (self.surface_size[0] - self.scroll_W) - self.H_bar_length # The amount of space the bar moves in pixels
        self.H_char_unit  = scrolling_space / self.CATH.max_line_chars    
        self.H_unit       = self.over_chars / scrolling_space             # Amount of pixel movement of bar per character
        self.char_unit    = scrolling_space / self.over_chars             # How many pixels to move scroll bar per character (with arrow keys)
        
        if self.mouse == 0:
            self.H_scroll_E   = self.char_unit * self.CATH.new_pos        # Keep Bar position updated (when not scroling with mouse)
        
        #Is mouse click inside scroll bar?
        if (self.mouse == 1 and self.mouseX > self.H_scroll_E and self.mouseX < (self.H_scroll_E + self.H_bar_length) and
            self.mouseY > (self.surface_size[1] - self.scroll_W) and self.mouseY < self.surface_size[1]
            and self.H_release == 0 and self.no_scroll == 0):
            
            # Create and grab some variables and get out of this loop
            self.window_move   = False
            self.temp_varH     = self.H_scroll_E
            self.H_scr_grab    = self.mouseX
            self.H_scr_grabbed = 1
            self.H_release     = 1
            self.H_col         = 50
            self.grab_char     = self.CATH.new_pos
            self.CATH.search   = 0
            self.CATH.no_entry = 1
            
        if self.H_scr_grabbed == 1: # The amount of X movement of the grabbed bar in pixels
            self.H_move = self.mouseX - self.H_scr_grab
            
            # If bar is back at top make sure to display text from line 1
            if self.H_scroll_E == 0:
                self.CATH.new_pos = 0
            
            # Convert pixel movement into characters scrolling
            # 'X amount of pixels scrolls Y amount of characters'
            if (self.H_scroll_E > 0 and
                self.H_scroll_E < self.H_scroll_E + self.H_bar_length):
                
                move              = self.H_scroll_E
                self.CATH.new_pos = round(move * self.H_unit)
            
            # Position of bar
            self.H_scroll_E = self.H_move + self.temp_varH
            
def render_Hscroll(self, surface):        
    # Draw Vertical Scroll Bar if we need too
    if self.longest_line > self.CATH.max_line_chars:
        
        # Keep the bar from leaving its Eastern and Western most regions
        if self.H_scroll_E < self.offset: self.H_scroll_E = self.offset
        if self.H_scroll_E > (self.surface_size[0] - self.scroll_W) - (self.H_bar_length + self.offset):
            self.H_scroll_E = (self.surface_size[0] - self.scroll_W) - (self.H_bar_length + self.offset)
        
        pygame.draw.rect(surface, Col("grey", self.H_col),
                        (self.H_scroll_E, self.surface_size[1] - self.scroll_W, self.H_bar_length, self.scroll_W))