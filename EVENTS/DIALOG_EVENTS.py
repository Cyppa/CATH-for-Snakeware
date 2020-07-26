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

from ..Editor.SHARED           import GOTO_line, clear_selected, save_load, go_home
from ..Editor.Cath_Editor      import update_text_info
from pygame_gui.windows      import UIConfirmationDialog, UIFileDialog
from pygame_gui.core.utility import create_resource_path

def confirmation(self, event, ui_manager):
    # Confirmation
    if (event.type == pygame.USEREVENT and
        event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED):
        
        # NewFile
        if event.ui_element == self.newfile_confirmation_dialog: 
            print("New File")
            
            if self.grid_was_on == 1: self.grid_on = 1
            self.grid_was_on = 0
            self.selectable  = 1
            file_path        = self.app_path + "/Editor/new.txt"
            save_load(self, 'open', file_path)
            #pygame.display.set_caption('CATH  ||  PyGame Text Editor')
            update_text_info(self.CATH)
            self.re_search = 1
        
        # Quit
        elif event.ui_element == self.confirmation_dialog_leave:
            
            pygame.quit()
            sys.exit()
        
        elif event.ui_element == self.confirmation_dialog_save:
            
            save_load(self, 'save', self.file_string)
            
            if self.save_error == False:
                self.editor_text = 0
                print('Good Bye! Save')
                time.sleep(1)
                self.running = False
                pygame.quit()  # quits pygame
                sys.exit()
            
            self.save_error    = False
            self.CATH.no_entry = 0
            
        elif event.ui_element == self.confirmation_dialog_no_save:
            
            self.editor_text = 0
            print('Good Bye! No save')
            time.sleep(1)
            self.running = False
            pygame.quit()  # quits pygame
            sys.exit()
         
        # Open File
        elif event.ui_element == self.confirmation_dialog_open:
            
            self.selectable    = 0
            self.editor_text   = 0
            if self.grid_on == 1: self.grid_was_on = 1
            
            self.file_dialog   = UIFileDialog(pygame.Rect(160, 50, 440, 500),
                                                 ui_manager,
                                                 window_title='Open File...',
                                                 initial_file_path='./',
                                                 allow_existing_files_only=True)
            self.mouse_updater  = 0
            self.CATH.open_file = 1
            self.editor_text    = 0
            self.grid_on        = 0
            
            self.mouse_updater  = 0
            self.CATH.open_file = 1
            self.grid_on        = 0
            clear_selected(self)
            
            self.file_open      = 1
            
            self.V_move     = 0
            self.scroll_TOP = self.V_scroll_Y
            self.temp_var   = 0
            self.V_scr_grabbed = 0
            self.V_scr_grab = [0,0]

    # File Dialogue
    if (event.type == pygame.USEREVENT and
        event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED):
        
        self.file_string = create_resource_path(event.text)
        self.re_search = 1
        
        if self.grid_was_on == 1: self.grid_on = 1
        self.grid_was_on = 0
        self.selectable  = 1
        
        if self.file_open == 1:
            
            # Test if we can open the file and see if its a text file...
            try:
                self.file = open(self.file_string)
                
                print(self.file.readlines()[0])
                
                self.file.close()
            
            except UnicodeDecodeError:
                self.top_label.set_text(("File Not A Valid Text File!!!")[:self.top_label_chars])
                print("Not a text file?")
                self.CATH.open_file = 0
            except pygame.error:
                print(pygame.error)
            
            else:
                try: self.top_label.set_text(("File Loaded")[:self.top_label_chars])
                except:pass
                
                print("LOADING...")
                save_load(self, 'open', self.file_string)
                #pygame.display.set_caption('CATH  ||  PyGame Text Editor || ' + self.file_string)
                update_text_info(self.CATH)
                
                go_home(self, ui_manager)
        
        elif self.file_save == 1:
            save_load(self, 'save', self.file_string)
            self.top_label.set_text(("FILE SAVED!")[:self.top_label_chars])
            go_home(self, ui_manager)
                
                
