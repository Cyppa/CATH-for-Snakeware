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

def update_Vscroll(self):
    
    ######### Scroll Bar - Home Made ;)
    # Do we need scrollbar, are there more lines of text in file than screen space?
    if len(self.CATH.lines) > self.CATH.max_lines:

        # Create some  needed variables
        self.body_Y         = self.surface_size[1] - self.offset
        total_Y             = len(self.CATH.lines)              # Total lines of text in file
        self.over_lines     = total_Y -self.CATH.max_lines - 1  # Amount of lines we need to scroll
        total               = self.CATH.max_lines / total_Y     # How many times do total file lines divide into screen space
        self.V_bar_length   = self.body_Y * total               # Scroll Bar Length
        scrolling_space     = self.body_Y - self.V_bar_length - self.V_scroll_Y
        self.V_line_unit    = scrolling_space  / total_Y
        self.V_unit         = self.over_lines / scrolling_space # Amount of pixel movement of bar per line
        self.line_unit      = scrolling_space / self.over_lines # How many pixels to move scroll bar per line (with arrow keys)
        
        if self.mouse == 0:
            self.scroll_TOP = (self.line_unit * self.CATH.real) + self.V_scroll_Y # Keep Bar position updated (when not scroling with mouse)
        
        # Is mouse click inside scroll bar?
        if (self.mouse == 1 and self.mouseX > self.V_scroll_X and self.mouseX < self.panel_W and
            self.mouseY > self.scroll_TOP and self.mouseY < self.scroll_TOP + self.V_bar_length
            and self.V_release == 0 and self.no_scroll == 0):
            # Create and grab some variables and get out of this loop
            self.window_move   = False
            self.temp_var      = self.scroll_TOP
            self.V_scr_grab    = self.mouseY
            self.V_scr_grabbed = 1
            self.V_release     = 1
            self.V_col         = 25
            self.grab_line     = self.CATH.real
            self.CATH.search   = 0
            self.grab_cursor   = [self.CATH.pos, self.CATH.display_pos,
                                  self.CATH.current_line, self.CATH.display_current_line]
            
        if self.V_scr_grabbed == 1: # The amount of Y movement of the grabbed bar in pixels
            self.V_move = self.mouseY - self.V_scr_grab 
            
            # If bar is back at top make sure to display text from line 1
            if self.scroll_TOP == self.V_scroll_Y:
                self.CATH.real = 0
            
            # Convert pixel movement into line scrolling
            # 'X amount of pixels scrolls Y amount of lines'
            if (self.scroll_TOP > self.V_scroll_Y and
                self.scroll_TOP < self.scroll_TOP + self.V_bar_length):
                
                move           = self.scroll_TOP - self.V_scroll_Y
                self.CATH.real = round(move * self.V_unit)
                    
            self.scroll_TOP =  self.V_move + self.temp_var
            
def render_Vscroll(self, surface):        
    # Draw Vertical Scroll Bar if we need too
    if len(self.CATH.lines) > self.CATH.max_lines:
        # Keep the bar from leaving its upper and lowest most regions
        if self.scroll_TOP < self.V_scroll_Y: self.scroll_TOP = self.V_scroll_Y
        if self.scroll_TOP > self.body_Y - self.V_bar_length:
            self.scroll_TOP = self.body_Y - self.V_bar_length
        
        pygame.draw.rect(surface,Col("grey", self.V_col),
                        (self.V_scroll_X - 1, self.scroll_TOP, self.scroll_W, self.V_bar_length))
