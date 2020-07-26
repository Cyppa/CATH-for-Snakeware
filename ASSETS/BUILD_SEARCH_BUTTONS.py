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
from pygame_gui.elements import UIButton
from pygame_gui.elements import UITextEntryLine

def rebuild_search(self, ui_manager, text_entryX):
    
    # SEARCH
    if self.search_down:
        self.search_down.kill()
        self.search_down = UIButton(pygame.Rect(round(text_entryX), 0,
                                                    self.buttonX // 2, self.buttonY),
                                 'DOWN', manager=ui_manager, container=self.status_panel)

    if self.search_up:
        self.search_up.kill()
        self.search_up = UIButton(pygame.Rect(round(text_entryX + self.buttonX / 2), 0,
                                                    self.buttonX // 2, self.buttonY),
                                 'UP', manager=ui_manager, container=self.status_panel)

    if self.replace:
        self.replace.kill()
        self.replace = UIButton(pygame.Rect(round(text_entryX + self.buttonX),
                                        0, self.buttonX, self.buttonY), 'Replace >',
                            manager=ui_manager, container=self.status_panel)

    if self.all:
        self.all.kill()
        self.all = UIButton(pygame.Rect(round((text_entryX * 2) + (self.buttonX * 2)), 0,
                                        self.buttonX // 2, self.buttonY),'All',
                            manager=ui_manager, container=self.status_panel)

    # Text Entry
    if self.text_entry_search:
        self.text_entry_search.kill()
        self.text_entry_search = UITextEntryLine(pygame.Rect((self.offset, 0),
                                                         (text_entryX, self.buttonY)),
                                      ui_manager, container=self.status_panel,
                                      object_id = "#search")
    
    if self.text_entry_replace:
        self.text_entry_replace.kill()
        self.text_entry_replace = UITextEntryLine(pygame.Rect(((text_entryX +
                                                            self.buttonX * 2), 0),
                                                          (text_entryX, self.buttonY)),
                                              ui_manager, container=self.status_panel,
                                              object_id = "#replace")
