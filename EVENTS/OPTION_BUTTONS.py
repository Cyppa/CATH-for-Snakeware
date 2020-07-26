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

from ..Editor.SHARED             import GOTO_line, clear_selected
from ..Editor.Cath_Editor_Extras import update_text_info, reset
from ..EVENTS.GUI_METHODS        import update_bg
from pygame_gui.elements       import UIButton

def option_buttons(self, event, ui_manager):    # PyGame_Gui Button Presses
    
    if (event.type == pygame.USEREVENT and
                event.user_type == pygame_gui.UI_BUTTON_PRESSED):

        if event.ui_element == self.numbers_button:
            
            self.numbers = (self.numbers + 1) % 2
            
            if self.numbers == 1:
                
                self.text_offset       =   self.text_size * 3
                self.CATH.width           =   self.Ewidth - self.text_offset
                self.CATH.X               =   self.EditorX + self.text_offset
                self.CATH.max_line_chars =   self.CATH.max_line_chars - 4
                update_text_info(self.CATH)
                
            elif self.numbers == 0:
                
                self.CATH.width           =   self.Ewidth
                self.CATH.X               =   self.EditorX
                self.CATH.max_line_chars =   self.CATH.max_line_chars + 4
                update_text_info(self.CATH)
            
        if event.ui_element == self.colours_button:
            
            self.theme_counter = (self.theme_counter + 1) % 3
            self.theme = 'ASSETS/themes/theme_' + self.themes[self.theme_counter] + '.json'
            self.cwd = os.getcwd()
            os.system('cp ' + self.cwd + '/' + self.theme + ' ' + self.default_theme)
            
            if self.theme_counter == 1: self.CATH.font_colour = "black"
            else: self.CATH.font_colour = "white"
            update_bg(self, self.size, ui_manager)
            
        if event.ui_element == self.text_button1:
            clear_selected(self)
            if self.text_size < 40:
                update_text_info(self.CATH)
                self.text_size += 2
                
                self.CATH.text_size      =   self.text_size
                self.CATH.max_line_chars =   round(self.Ewidth / (self.text_size / 2)) - 3
                self.CATH.max_lines      =   round((self.Eheight)/ self.text_size) - 1
                self.CATH.text_width     =   round(self.text_size / 2)
                reset(self.CATH)
                
                if len(self.CATH.lines) > self.CATH.max_lines:
                    self.CATH.total_lines = self.CATH.max_lines
                else: self.CATH.total_lines = len(self.CATH.lines)
                    
                self.CATH.update_display(0)
                
                GOTO_line(self, self.CATH.current_line)
                self.top_label.set_text(("TEXT SIZE: " + str(self.text_size))[:self.top_label_chars])
                print('chars',self.CATH.max_line_chars ,'lines',self.CATH.max_lines)
                
                
        if event.ui_element == self.text_button2:
            clear_selected(self)
            if self.text_size > 8:
                self.text_size -= 2
                
                self.CATH.text_size      =   self.text_size
                self.CATH.max_line_chars =   round(self.Ewidth / (self.text_size / 2)) - 3
                self.CATH.max_lines      =   round((self.Eheight)/ self.text_size) - 1
                self.CATH.text_width     =   round(self.text_size / 2)
                
                if len(self.CATH.lines) > self.CATH.max_lines:
                    self.CATH.total_lines = self.CATH.max_lines
                else: self.CATH.total_lines = len(self.CATH.lines)
                
                self.CATH.update_display(0)
                self.top_label.set_text(("TEXT SIZE: " + str(self.text_size))[:self.top_label_chars])
                print('chars',self.CATH.max_line_chars ,'lines',self.CATH.max_lines)
        
        if event.ui_element == self.cursor_button:
            
            self.cursor_on = (self.cursor_on + 1) % 2
            if self.cursor_on == 0: cur_text = "Box Cursor OFF"
            else: cur_text = "Box Cursor ON"
            self.top_label.set_text((cur_text)[:self.top_label_chars])
            
        if event.ui_element == self.clear_history_button:
            with open("./cache.txt", 'w') as cache:
                pass
                #print("[[\n\n]]\n", file = cache)
            self.top_label.set_text(("HIST. CLEARDED!")[:self.top_label_chars])
    
    # Horizontal Slider
    if (event.type == pygame.USEREVENT and
                event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED): 
        
            if event.ui_element == self.grid_slider:
                self.grid_strength = event.value
                
                if self.grid_strength == 0:
                    self.grid_on = 0
                else: self.grid_on = 1
                


