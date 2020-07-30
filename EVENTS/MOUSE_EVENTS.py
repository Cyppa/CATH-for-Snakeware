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

import pygame

from ..Editor.Cath_Editor_Extras import update_text_info
from ..EVENTS.GUI_METHODS        import status_update
from ..Editor.SHARED             import clear_selected
from ..EVENTS.GUI_SELECT         import build_selection
              
def update_events_mouse(self, event):

    # Get Mouse Position and add relative offset (window XY)
    
    x, y        = pygame.mouse.get_pos()
    x           = x + self.rel_X - self.EditorX
    y           = y + self.rel_Y - (self.EditorY + self.bar_width)
    self.mouseX = x
    self.mouseY = y + self.EditorY
    
    #self.top_label.set_text(str(self.mouse_X + 1)+":"+str(self.mouse_Y))
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        self.mouse = 1
        
        #print('self.mouseX', self.mouseX,'self.mouseY', self.mouseY)
        # Check if mouse click is in writeable area
        if (x > 0 and x < (self.surface_size[0] - self.scroll_W) and y > 0 and
            y < (self.surface_size[1]- self.scroll_W)):
            
            self.scrolled      = 0
            self.CATH.no_entry = 0
            
            # Get clicks at centre of character by creating an offset
            x = x - (self.CATH.text_width // 2)
            y = y + (self.CATH.text_width // 2)
            
            self.character_X = round(x / self.CATH.text_width)
            self.line_Y      = round(y / self.text_size)
            
            # Make sure cursor line position is less than total amount of lines
            if self.line_Y > len(self.CATH.lines):
                self.line_Y = len(self.CATH.lines) - 1
            
            # Update cursor position in text editor
            # Get some info whether we click inside writeable area
            surface_size     = self.get_container().get_size()
            hit_Y            = y + self.EditorY
            
            # Make sure click is inside text area
            if hit_Y < surface_size[1]:
            
                # Make sure cursor falls inside line length
                
                line_length    = len(self.CATH.lines[self.line_Y + self.CATH.real - 1])
                real_X_pos     = self.character_X + self.CATH.new_pos
                relative_X_pos = self.character_X
                
                if real_X_pos > line_length:
                    
                    self.CATH.pos = line_length
                    
                else:
                    self.CATH.pos         = self.character_X + self.CATH.new_pos   # Actual character position
                if self.move_lines > 0: XY = 1
                else                  : XY = 0
                
                self.CATH.current_line         = self.line_Y + self.CATH.real #self.move_lines# - XY# + self.move_lines # Actual line number, included scrolled offset
                self.CATH.display_current_line = self.line_Y                                    # Screen line number
                
                
                #update_text_info(self.CATH)
        else: self.CATH.no_entry = 1
        
    if event.type == pygame.MOUSEBUTTONUP:
        
        # Check if we need to clear selection
        if (self.sel_start[0] == self.mouse_X + self.CATH.new_pos and
            self.sel_start[1] == self.mouse_Y + self.CATH.real):
            
            self.selecting     = 0
            self.selected = 0
            clear_selected(self)
            
        elif self.V_scr_grabbed == 0 and self.H_scr_grabbed == 0:
            
            self.sel_end = [self.mouse_X + self.CATH.new_pos, self.mouse_Y + self.CATH.real]
            self.release_line_len = len(self.CATH.lines[self.sel_end[1] - 1])
            
            if self.sel_end[0] > self.release_line_len:
                self.sel_end[0] = self.release_line_len
            self.selected =1
            build_selection(self)
        
        self.V_col         = 100
        self.H_col         = 100
        self.mouse         = 0
        self.scrolling     = 0
        self.V_scr_grabbed = 0
        self.V_release     = 0
        self.H_release     = 0
        self.H_scr_grabbed = 0
        self.sel_loop      = 0
        self.select_scroll = 0
        self.no_scroll     = 0

