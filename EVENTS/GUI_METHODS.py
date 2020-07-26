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
from pygame_gui.elements.ui_image import UIImage

# Update stat info label
def status_update(self, mouse_X = 1, mouse_Y = 1):
    
    pos            = self.CATH.get_pos() # CATH method to get updated info
    self.cur_pos   = pos[0] + 1
    self.line_pos  = pos[1]
    self.chars     = pos[2] + 1
    self.all_lines = pos[3]
    caps           = pos[4]
    
    if caps == 0: self.caps = "OFF"
    else        : self.caps = " ON"
    
    if mouse_Y > 0:
        self.status_text = ("Line: " + str(self.line_pos) + " / " + str(self.all_lines) +
                            "  ||  Pos: " + str(self.cur_pos) + " / " + str(self.chars) +
                            "  ||  CAPS: " +  str(self.caps) + "  ||  MOUSE: " + str(mouse_X)
                            + ", " + str(mouse_Y))        
    
    self.stats.set_text(self.status_text[:self.stat_label_chars])

# Text background updater
def update_bg(self, size, ui_manager):
    
    size = self.get_container().get_size()
    # Create background asset
    self.surface_element = UIImage(pygame.Rect((0, 0), size),
                                            pygame.Surface(size).convert(),
                                            manager=ui_manager,
                                            container=self,
                                            parent_element=self)
    
    self.background = pygame.Surface(size)  # make a background surface
    self.background = self.background.convert()
    if   self.theme_counter == 1: BG = (255, 255, 255)
    elif self.theme_counter == 2: BG = (0, 0, 0)
    else: BG = ui_manager.ui_theme.get_colour('dark_bg') # Fix default BG colouring...
    self.background.fill(BG)
    
