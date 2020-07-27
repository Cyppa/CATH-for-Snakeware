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

## STATUS BUTTONS
def build_home_assets(self, ui_manager):    
    # HOME
    if self.goto_button:
        self.goto_button.kill()
        self.goto_button = UIButton(pygame.Rect(0, 0, self.buttonX,
                                        self.buttonY), 'GOTO', manager=ui_manager,
                            container=self.status_panel)

    if self.text_entry_goto:
        self.text_entry_goto.kill()
        self.text_entry_goto = UITextEntryLine(pygame.Rect((self.buttonX, 0),
                                              (self.buttonX, self.buttonY)),
                                  ui_manager, container=self.status_panel)
        
    self.status_text = ("")

    if self.stats:
        self.stats.kill()
        self.stats = UILabel(pygame.Rect((self.buttonX * 2), 0,
                                     self.label_W, self.buttonY),
                         self.status_text, manager=ui_manager, container=self.status_panel,
                         anchors={'top': 'top', 'bottom': 'top',
                                       'left': 'left', 'right': 'right'})

def build_disk_assets(self, ui_manager):
    # DISK
    if self.save_button:
        self.save_button.kill()
        self.save_button = UIButton(pygame.Rect(0, 0, self.buttonX,self.buttonY), 'Save File',
                            manager=ui_manager, container=self.status_panel)

    if self.open_button:
        self.open_button.kill()
        self.open_button = UIButton(pygame.Rect(self.buttonX, 0, self.buttonX,
                                            self.buttonY),
                                'Open File', manager=ui_manager, container=self.status_panel)

    if self.new_file_button:
        self.new_file_button.kill()
        self.new_file_button = UIButton(pygame.Rect((self.buttonX *2), 0, self.buttonX,
                                            self.buttonY),
                                'New File', manager=ui_manager, container=self.status_panel)

def build_options_assets(self, ui_manager):
    # OPTIONS
    if self.numbers_button:
        self.numbers_button.kill()
        self.numbers_button = UIButton(pygame.Rect(0, 0,
                                               int(self.buttonX//2), self.buttonY),
                                   'Numbr', manager=ui_manager, container=self.status_panel)

    if self.colours_button:
        self.colours_button.kill()
        self.colours_button = UIButton(pygame.Rect(self.buttonX, 0,
                                               self.buttonX, self.buttonY), 'Colours',
                            manager=ui_manager, container=self.status_panel)

    if self.text_button2:
        self.text_button2.kill()
        self.text_button2 = UIButton(pygame.Rect((self.buttonX * 2), 0,
                                             self.buttonX//2, self.buttonY), 'Text-',
                            manager=ui_manager, container=self.status_panel)

    if self.text_button1:
        self.text_button1.kill()
        self.text_button1 = UIButton(pygame.Rect(round(self.buttonX * 2.5), 0,
                                             self.buttonX//2, self.buttonY),
                                 'Text+', manager=ui_manager, container=self.status_panel)

    if self.cursor_button:
        self.cursor_button.kill()
        self.cursor_button = UIButton(pygame.Rect(int(self.buttonX//2), 0,
                                             int(self.buttonX//2), self.buttonY),
                                 'Cursr', manager=ui_manager, container=self.status_panel)

    if self.clear_history_button:
        self.clear_history_button.kill()
        self.clear_history_button = UIButton(pygame.Rect((self.buttonX *3), 0,
                                             int(self.buttonX//2), self.buttonY),
                                 'Hist.', manager=ui_manager, container=self.status_panel)
    
    ### LABEL
    self.grid_label = UILabel(pygame.Rect(round(3.5 * self.buttonX), 0, (self.buttonX // 2),
                                 self.buttonY), "GRID:" ,ui_manager,
                     container=self.status_panel)
    
    ### Horizontal Slider
    if self.grid_slider:
        self.grid_slider.kill()
        self.grid_slider = UIHorizontalSlider(pygame.Rect((4 * self.buttonX), 0,
                                                      self.panel_W - (4 * self.buttonX) - 6, self.buttonY),
                                          start_value = 0, value_range = (0, 255),
                                          manager = ui_manager, container = self.status_panel,
                                          anchors={'top': 'top', 'bottom': 'bottom',
                                                   'left': 'left', 'right': 'right'})
    
def build_search_assets(self, ui_manager):
    # SEARCH
    if self.search_down:
        self.search_down.kill()
        self.search_down = UIButton(pygame.Rect(round(self.text_entryX), 0,
                                                    self.buttonX // 2, self.buttonY),
                                 'DOWN', manager=ui_manager, container=self.status_panel)

    if self.search_up:
        self.search_up.kill()
        self.search_up = UIButton(pygame.Rect(round(self.text_entryX + self.buttonX / 2), 0,
                                                    self.buttonX // 2, self.buttonY),
                                 'UP', manager=ui_manager, container=self.status_panel)

    if self.replace:
        self.replace.kill()
        self.replace = UIButton(pygame.Rect(round(self.text_entryX + self.buttonX),
                                        0, self.buttonX, self.buttonY), 'Replace >',
                            manager=ui_manager, container=self.status_panel)

    if self.all:
        self.all.kill()
        self.all = UIButton(pygame.Rect(round((self.text_entryX * 2) + (self.buttonX * 2)),
                                        0, self.buttonX // 2, self.buttonY),'All',
                            manager=ui_manager, container=self.status_panel)
        
     # Text Entry
    if self.text_entry_search:
        self.text_entry_search.kill()
        self.text_entry_search = UITextEntryLine(pygame.Rect((self.offset, 0),
                                                         (self.text_entryX, self.buttonY)),
                                      ui_manager, container=self.status_panel,
                                      object_id = "#search")

    if self.text_entry_replace:
        self.text_entry_replace.kill()
        self.text_entry_replace = UITextEntryLine(pygame.Rect(((self.text_entryX +
                                                            self.buttonX * 2), 0),
                                                          (self.text_entryX, self.buttonY)),
                                              ui_manager, container=self.status_panel,
                                              object_id = "#replace")

def build_quit_assets(self, ui_manager):    
    # QUIT
    if self.quit_button_save:
        self.quit_button_save.kill()
        self.quit_button_save    = UIButton(pygame.Rect( (-self.buttonX) * 1, 0,
                                                    self.buttonX, self.buttonY),
                                        'SAVE & QUIT', manager=ui_manager,
                                        container=self.status_panel, anchors=
                                            {'top': 'top', 'bottom': 'bottom',
                                       'left': 'right', 'right': 'right'})

    if self.quit_button_no_save:
        self.quit_button_no_save.kill()
        self.quit_button_no_save = UIButton(pygame.Rect((-self.buttonX) * 2, 0,
                                                    self.buttonX, self.buttonY),
                                        'JUST QUIT', manager=ui_manager,
                                        container=self.status_panel, anchors=
                                            {'top': 'top', 'bottom': 'bottom',
                                       'left': 'right', 'right': 'right'})
     
