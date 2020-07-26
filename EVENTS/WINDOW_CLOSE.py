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
import sys, time

from datetime           import datetime
from ..Editor.SHARED      import save_load, go_home
from pygame_gui.windows import UIConfirmationDialog, UIFileDialog

### QUIT 
def LEAVE(self, event, ui_manager, string = ""):
    
    self.selectable  = 0
    #clear_selected(self)
    self.confirmation_dialog_leave = UIConfirmationDialog(pygame.Rect((self.size[0] // 2) - 130,
                                                (self.size[1] //2) - 100, 260, 200),
                ui_manager,
                "SAVED: " + string,
                window_title='Just Quit...',
                blocking = True,
                object_id = '#QuitConfirmLeave')
    #time.sleep(2)
    #sys.exit()
    self.editor_text = 0

def close_window(self, event, ui_manager):
    
    if (event.type == pygame.USEREVENT and
        event.user_type == pygame_gui.UI_BUTTON_PRESSED
        and event.ui_object_id == '#window.#close_button'):
            pass
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y_%H-%M-%S")
            file = "./Backups/FILE_" + timestampStr + ".txt"
            save_load(self, 'save', file)
            LEAVE(self, event, ui_manager, file)    
            print("Window closed... Time to quit")
            
# WINDOW CLOSE EVENTS
def window_close_events(self, event):
    
    if (event.type == pygame.USEREVENT and
        event.user_type ==pygame_gui.UI_WINDOW_CLOSE):
        
        # Quit No Save
        if (event.ui_element == self.confirmation_dialog_no_save or
             event.ui_element == self.confirmation_dialog_save):
            
            if self.grid_was_on == 1: self.grid_on = 1
            
            self.grid_was_on   = 0
            self.editor_text   = 1
            self.mouse_updater = 1
            self.selectable    = 1
            
            self.quit_button.enable()
            self.confirmation_dialog_no_save = None
            self.confirmation_dialog_save    = None
        
        # New File
        if event.ui_element == self.newfile_confirmation_dialog:
            
            if self.grid_was_on == 1: self.grid_on = 1
            
            self.grid_was_on   = 0
            self.editor_text   = 1
            self.mouse_updater = 1
            self.selectable    = 1
            
            self.newfile_confirmation_dialog = None
            self.new_file_button.enable()
            go_home(self, self.ui_manager)
            
        # File
        if event.ui_element == self.file_dialog:
            
            if self.grid_was_on == 1: self.grid_on = 1
            
            self.open_button.enable()
            self.save_button.enable()
            self.new_file_button.enable()
            
            self.file_dialog    = None
            self.CATH.file_save = 0
            self.CATH.file_open = 0
            self.file_save      = 0
            self.file_open      = 0
            self.editor_text    = 1
            self.mouse_updater  = 1
            self.selectable     = 1
            self.re_search      = 1
            self.grid_was_on    = 0
            
        # File open cancel
        if event.ui_element == self.confirmation_dialog_open:
            
            if self.file_dialog == None:
                
                if self.grid_was_on == 1: self.grid_on = 1
                
                self.grid_was_on    = 0
                self.mouse_updater  = 1
                self.CATH.open_file = 0
                self.editor_text    = 1
                self.file_open      = 0
                self.selectable     = 1
                
                self.open_button.enable()
                self.save_button.enable()
                self.new_file_button.enable()
            
            self.confirmation_dialog_open = None
