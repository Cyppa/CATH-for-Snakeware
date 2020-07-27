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

from pygame_gui.elements import UIButton
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIPanel
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIHorizontalSlider

def create_assets(self, ui_manager):
    
    self.confirmation_dialog_no_save = None
    self.confirmation_dialog_save    = None
    self.newfile_confirmation_dialog = None
    self.confirmation_dialog_open    = None
    self.file_dialog                 = None
    self.confirmation_dialog_leave   = None
    
    offset = self.offset

    ## PANELS
    self.top_panel = UIPanel(pygame.Rect(offset, offset, self.panel_W - (offset * 2), self.buttonY + (offset * 6)),
                         starting_layer_height=4,
                         manager=ui_manager,container=self,
                              anchors={'top': 'top', 'bottom': 'top',
                                       'left': 'left', 'right': 'right'})

    self.status_panel = UIPanel(pygame.Rect(offset, self.buttonY + (offset * 2),
                                            self.panel_W - (offset * 2), self.buttonY + (offset * 3)),
                         starting_layer_height=4,
                         manager=ui_manager,container=self,
                              anchors={'top': 'top', 'bottom': 'top',
                                       'left': 'left', 'right': 'right'})
    
    self.hidden_panel = UIPanel(pygame.Rect(-1000, -1000, 800, 100),
                         starting_layer_height=0,
                         manager=ui_manager,container=self)
    
    ## TOP PANEL BUTTONS
    self.home_button = UIButton(pygame.Rect(0, 0, self.buttonX, self.buttonY),
                                'HOME', manager=ui_manager,
                                container=self.top_panel)
    self.home_button.disable()

    self.disk_button = UIButton(pygame.Rect(self.buttonX, 0, self.buttonX, self.buttonY),
                                'DISK', manager=ui_manager,
                                container=self.top_panel)

    self.options_button = UIButton(pygame.Rect(self.buttonX * 2, 0, self.buttonX, self.buttonY),
                                'OPTIONS', manager=ui_manager,
                                container=self.top_panel)

    self.search_button = UIButton(pygame.Rect(self.buttonX * 3, 0, self.buttonX, self.buttonY),
                                'SEARCH', manager=ui_manager,
                                container=self.top_panel)

    self.top_label = UILabel(pygame.Rect((4 * self.buttonX), 0, self.panel_W - (5 * self.buttonX),
                                 self.buttonY), "" ,ui_manager,
                     container=self.top_panel,anchors={'top': 'top', 'bottom': 'top',
                                       'left': 'left', 'right': 'right'})

    self.quit_button = UIButton(pygame.Rect(-self.buttonX, 0, self.buttonX, self.buttonY),
                                'QUIT', manager=ui_manager,
                                container=self.top_panel, anchors=
                                {'top': 'top', 'bottom': 'bottom',
                                       'left': 'right', 'right': 'right'})
    
    #HOME
    self.goto_button = UIButton(pygame.Rect(0, 0, self.buttonX,
                                        self.buttonY), 'GOTO', manager=ui_manager,
                            container=self.status_panel)

    self.text_entry_goto = UITextEntryLine(pygame.Rect((self.buttonX, 0),
                                              (self.buttonX, self.buttonY)),
                                  ui_manager, container=self.status_panel)
        
    self.status_text = ("STATS")

    self.stats = UILabel(pygame.Rect((self.buttonX * 2), 0,
                                     self.panel_W - (self.offset * 2) - (self.buttonX * 2), self.buttonY),
                         self.status_text, manager=ui_manager, container=self.status_panel,
                         anchors={'top': 'top', 'bottom': 'top',
                                       'left': 'left', 'right': 'right'})
    # DISK
    self.save_button = UIButton(pygame.Rect(0, 0, self.buttonX,self.buttonY), 'Save File',
                            manager=ui_manager, container=self.hidden_panel)

   
    self.open_button = UIButton(pygame.Rect(self.buttonX, 0, self.buttonX,
                                            self.buttonY),
                                'Open File', manager=ui_manager, container=self.hidden_panel)


    self.new_file_button = UIButton(pygame.Rect((self.buttonX *2), 0, self.buttonX,
                                            self.buttonY),
                                'New File', manager=ui_manager, container=self.hidden_panel)
    
    # OPTIONS
    self.numbers_button = UIButton(pygame.Rect(0, 0,
                                               int(self.buttonX//2), self.buttonY),
                                   'Numbr', manager=ui_manager, container=self.hidden_panel)

    self.colours_button = UIButton(pygame.Rect(self.buttonX, 0,
                                               self.buttonX, self.buttonY), 'Colours',
                            manager=ui_manager, container=self.hidden_panel)

    self.text_button2 = UIButton(pygame.Rect((self.buttonX * 2), 0,
                                             self.buttonX//2, self.buttonY), 'Text-',
                            manager=ui_manager, container=self.hidden_panel)

    self.text_button1 = UIButton(pygame.Rect(round(self.buttonX * 2.5), 0,
                                             self.buttonX//2, self.buttonY),
                                 'Text+', manager=ui_manager, container=self.hidden_panel)

    self.cursor_button = UIButton(pygame.Rect(int(self.buttonX//2), 0,
                                             int(self.buttonX//2), self.buttonY),
                                 'Cursr', manager=ui_manager, container=self.hidden_panel)

    self.clear_history_button = UIButton(pygame.Rect((self.buttonX *3), 0,
                                             int(self.buttonX//2), self.buttonY),
                                 'Hist.', manager=ui_manager, container=self.hidden_panel)
    ### LABEL
    self.grid_label = UILabel(pygame.Rect(round(3.5 * self.buttonX), 0, (self.buttonX // 2),
                                 self.buttonY), "GRID:" ,ui_manager,
                     container=self.hidden_panel)
    
    ### Horizontal Slider
    self.grid_slider = UIHorizontalSlider(pygame.Rect((5 * self.buttonX), 0,
                                                      self.buttonX, self.buttonY),
                                          start_value = 0, value_range = (0, 255),
                                          manager = ui_manager, container = self.hidden_panel,
                                          anchors={'top': 'top', 'bottom': 'bottom',
                                                   'left': 'left', 'right': 'right'})
    
    # SEARCH
    self.search_down = UIButton(pygame.Rect(round(self.text_entryX), 0,
                                                    self.buttonX // 2, self.buttonY),
                                 'DOWN', manager=ui_manager, container=self.hidden_panel)

    self.search_up = UIButton(pygame.Rect(round(self.text_entryX + self.buttonX / 2), 0,
                                                    self.buttonX // 2, self.buttonY),
                                 'UP', manager=ui_manager, container=self.hidden_panel)

    self.replace = UIButton(pygame.Rect(round(self.text_entryX + self.buttonX),
                                        0, self.buttonX, self.buttonY), 'Replace >',
                            manager=ui_manager, container=self.hidden_panel)

    self.all = UIButton(pygame.Rect(round((self.text_entryX * 2) + (self.buttonX * 2)),
                                        0, self.buttonX // 2, self.buttonY),'All',
                            manager=ui_manager, container=self.hidden_panel)
        
    # Text Entry
    self.text_entry_search = UITextEntryLine(pygame.Rect((self.offset, 0),
                                                         (self.text_entryX, self.buttonY)),
                                      ui_manager, container=self.hidden_panel,
                                      object_id = "#search")

    self.text_entry_replace = UITextEntryLine(pygame.Rect(((self.text_entryX +
                                                            self.buttonX * 2), 0),
                                                          (self.text_entryX, self.buttonY)),
                                              ui_manager, container=self.hidden_panel,
                                              object_id = "#replace")
    
    # QUIT
    self.quit_button_save    = UIButton(pygame.Rect( (-self.buttonX) * 1, 0,
                                                    self.buttonX, self.buttonY),
                                        'SAVE & QUIT', manager=ui_manager,
                                        container=self.hidden_panel, anchors={'top': 'top', 'bottom': 'bottom',
                                       'left': 'right', 'right': 'right'})

    self.quit_button_no_save = UIButton(pygame.Rect((-self.buttonX) * 2, 0,
                                                    self.buttonX, self.buttonY),
                                        'JUST QUIT', manager=ui_manager,
                                        container=self.hidden_panel, anchors={'top': 'top', 'bottom': 'bottom',
                                       'left': 'right', 'right': 'right'})
    
    print('GUI ASSETS Created')