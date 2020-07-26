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
import pygame_gui
import time, sys, os

from ..Editor.SHARED             import GOTO_line
from ..Editor.Cath_Editor_Search import search_text, replace_text
from pygame_gui.elements       import UIButton

def search_buttons(self, event):
    
    if (event.type == pygame.USEREVENT and
                event.user_type == pygame_gui.UI_BUTTON_PRESSED):
       
       #SEARCH
        if event.ui_element == self.search_down:
            
            search_text(self, self.search_string, "down")
            self.CATH.search        = 1
            self.CATH.cursor_length = len(self.search_string)
            self.CATH.re_search     = 0
        
        if event.ui_element == self.search_up:
            
            search_text(self, self.search_string, "up")
            self.CATH.search        = 1
            self.CATH.cursor_length = len(self.search_string)
            self.CATH.re_search     = 0
            
        if event.ui_element == self.replace:
            
            replace_text(self, self.replace_string, "once")
            self.CATH.search        = 1
            self.CATH.cursor_length = len(self.search_string)
            self.CATH.re_search     = 0
        
        if event.ui_element == self.all:
            
            replace_text(self, self.replace_string, "all")
            self.CATH.search        = 1
            self.CATH.cursor_length = len(self.search_string)
            self.CATH.re_search     = 0
            
            
