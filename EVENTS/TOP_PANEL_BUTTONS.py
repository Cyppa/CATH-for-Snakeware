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

from pygame_gui.elements     import UIButton
from pygame_gui.windows      import UIFileDialog
from pygame_gui.windows      import UIConfirmationDialog

from ..ASSETS.ASSETS_REBUILDER import build_home_assets, build_disk_assets, build_options_assets
from ..ASSETS.ASSETS_REBUILDER import build_search_assets, build_quit_assets

def go_home(self, ui_manager):
    # Home Screen
    home_hide = [self.numbers_button, self.colours_button, self.save_button, self.cursor_button,
                 self.open_button, self.text_button1, self.grid_slider, self.grid_label,
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

def top_panel_buttons(self, event, ui_manager):    # PyGame_Gui Button Presses
    
    if (event.type == pygame.USEREVENT and
                event.user_type == pygame_gui.UI_BUTTON_PRESSED):
    
        # QUIT
        if event.ui_element == self.quit_button:
            
            self.search_button_pressed = False            
            quit_hide = [self.numbers_button, self.colours_button, self.save_button, self.stats,
                         self.open_button, self.text_button1, self.grid_label,
                         self.text_button2, self.grid_slider,
                         self.text_entry_search, self.search_down, self.search_up,
                         self.text_entry_replace, self.replace, self.all, self.cursor_button,
                         self.goto_button, self.text_entry_goto, self.new_file_button, self.clear_history_button]
            
            for item in quit_hide: item.kill()
            
            build_quit_assets(self, ui_manager)
            
            self.home_button.enable()
            self.options_button.enable()
            self.disk_button.enable()
            self.quit_button.disable()
            self.search_button.enable()
        
        # HOME
        if event.ui_element == self.home_button:
            
            self.search_button_pressed = False
            go_home(self, ui_manager)
                
        # OPTIONS
        if event.ui_element == self.options_button:
            
            self.search_button_pressed = False            
            options_hide = [self.save_button, self.open_button, self.stats,
                            self.quit_button_no_save, self.quit_button_save,
                            self.text_entry_search, self.search_down, self.search_up,
                            self.text_entry_replace, self.replace, self.all,
                            self.goto_button, self.text_entry_goto, self.new_file_button]
            
            for item in options_hide: item.kill()
                
            build_options_assets(self, ui_manager)
            
            self.home_button.enable()
            self.options_button.disable()
            self.disk_button.enable()
            self.quit_button.enable()
            self.search_button.enable()
        
        # DISK
        if event.ui_element == self.disk_button:
            
            self.search_button_pressed = False
            disk_hide = [self.numbers_button, self.colours_button, self.grid_label,
                         self.text_button1, self.text_button2, self.stats,
                         self.quit_button_save, self.text_entry_search, self.quit_button_no_save,
                         self.search_down, self.search_up, self.grid_slider,
                         self.text_entry_replace, self.replace, self.all, self.goto_button,
                         self.text_entry_goto, self.cursor_button,
                         self.clear_history_button]
            
            for item in disk_hide: item.kill()
            
            build_disk_assets(self, ui_manager)
            
            self.home_button.enable()
            self.options_button.enable()
            self.disk_button.disable()
            self.quit_button.enable()
            self.search_button.enable()
            
        # SEARCH
        if event.ui_element == self.search_button:
            
            self.search_button_pressed = True
            search_hide = [self.numbers_button, self.colours_button, self.save_button,
                           self.open_button, self.text_button1, self.stats, self.grid_label,
                           self.text_button2, self.quit_button_no_save, self.quit_button_save,
                           self.goto_button, self.text_entry_goto, self.grid_slider,
                           self.cursor_button, self.new_file_button, self.clear_history_button]
            
            build_search_assets(self, ui_manager)
            
            self.search_button.disable()
            self.home_button.enable()
            self.options_button.enable()
            self.quit_button.enable()
            self.disk_button.enable()
            
            for item in search_hide: item.kill()
            
