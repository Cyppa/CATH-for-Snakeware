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

from ..Editor.SHARED       import GOTO_line
from pygame_gui.elements import UIButton
from pygame_gui.windows  import UIFileDialog
from pygame_gui.windows  import UIConfirmationDialog

def bottom_panel_buttons(self, event, ui_manager):    # PyGame_Gui Button Presses
    
    if (event.type == pygame.USEREVENT and
                event.user_type == pygame_gui.UI_BUTTON_PRESSED):
        
        ## GOTO BUTTON
        if event.ui_element == self.goto_button:
            try:
                integer = int(self.goto_string)
                GOTO_line(self, integer)
            except (ValueError, AttributeError): self.top_label.set_text(("INVALID INPUT!")[:self.top_label_chars])
            else: pass
        
        if event.ui_element == self.quit_button_save:
            
            if self.grid_on == 1: self.grid_was_on = 1
            
            self.selectable    = 0
            self.file_save     = 1
            self.editor_text   = 0
            self.mouse_updater = 0
            self.grid_on       = 0
            #clear_selected(self)
            
            self.confirmation_dialog_save = UIConfirmationDialog(pygame.Rect((self.size[0] // 2) - 130,
                                                            (self.size[1] //2) - 100, 260, 200),
                            ui_manager,
                            "Are you sure you want to Save File and QUIT?",
                            window_title='Save And Quit...',
                            blocking = True,
                            object_id = '#QuitSaveConfirm')
            
        if event.ui_element == self.quit_button_no_save:
            
            if self.grid_on == 1: self.grid_was_on = 1
            
            self.selectable    = 0
            self.mouse_updater = 0    
            self.editor_text   = 0
            self.grid_on       = 0
            #clear_selected(self)
            self.confirmation_dialog_no_save = UIConfirmationDialog(pygame.Rect((self.size[0] // 2) - 130,
                                                (self.size[1] //2) - 100, 260, 200),
                ui_manager,
                "Are you sure you want to Quit WITHOUT Saving?",
                window_title='Just Quit...',
                blocking = True,
                object_id = '#QuitConfirm')
            
        # Open
        if event.ui_element == self.open_button:
            
            self.file_open  = 1
            self.selectable = 0
            #clear_selected(self)
            self.confirmation_dialog_open = UIConfirmationDialog(pygame.Rect((self.size[0] // 2) - 130,
                                                            (self.size[1] //2) - 100, 260, 200),
                            ui_manager,
                            "Unsaved changes to current file WILL be lost...",
                            window_title='OPEN?...',
                            blocking = True,
                            object_id = '#OpenConfirm')
                        
            self.open_button.disable()
            self.save_button.disable()
            self.new_file_button.disable()
            self.editor_text = 0
        
        # Save
        if event.ui_element == self.save_button:
            
            if self.grid_on == 1: self.grid_was_on = 1
            
            self.selectable       = 0
            self.grid_on          = 0
            self.mouse_updater    = 0
            self.CATH.save_file   = 1
            #clear_selected(self)
            self.file_dialog      = UIFileDialog(pygame.Rect(160, 50, 440, 500),
                                                 ui_manager,
                                                 window_title='Save File...',
                                                 initial_file_path='./',
                                                 allow_existing_files_only=False)
            self.open_button.disable()
            self.save_button.disable()
            self.new_file_button.disable()
            self.file_save   = 1
            self.editor_text = 0
        
        # New File
        if event.ui_element == self.new_file_button:
            
            if self.grid_on == 1: self.grid_was_on = 1
            
            self.re_search   = 0
            self.selectable  = 0
            self.editor_text = 0
            self.grid_on     = 0
            #clear_selected(self)
            self.new_file_button.disable()
            
            self.newfile_confirmation_dialog = UIConfirmationDialog(pygame.Rect((self.size[1] // 2) - 130,
                                                                (self.size[1] //2) - 100, 260, 200),
                                ui_manager,
                                "Create A New File? Any Unsaved Changes Will Be Lost!",
                                window_title='NEW FILE...',
                                blocking = True,
                                object_id = '#NewFileConfirm')
            
            
