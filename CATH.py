#######################################################################################################
#    CATH - A text editor written in python, pygame and pygame_gui
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
#    By Cyprian.
#    home@cyprian.com.au
#
#    DISCLAIMER!!!!!!
#    This is in very early stages of development. It WILL break as it is a 'proof of concept'
#    version and should not be used for anything but testing and exploring... 
#
#######################################################################################################

import pygame
import pygame_gui
import os

from pygame.locals                 import *
from .EVENTS.TOP_PANEL_BUTTONS     import top_panel_buttons
from .EVENTS.BOTTOM_PANEL_BUTTONS  import bottom_panel_buttons
from .EVENTS.WINDOW_CLOSE          import close_window, window_close_events
from .EVENTS.GUI_METHODS           import status_update, update_bg
from .EVENTS.DIALOG_EVENTS         import confirmation
from .EVENTS.MOUSE_EVENTS          import update_events_mouse
from .EVENTS.TEXT_ENTRY            import text_entry
from .EVENTS.SEARCH_BUTTONS        import search_buttons
from .EVENTS.OPTION_BUTTONS        import option_buttons
from .EVENTS.V_SCROLL              import update_Vscroll, render_Vscroll
from .EVENTS.H_SCROLL              import update_Hscroll, render_Hscroll
from .EVENTS.WINDOW                import update_window_size, window_move_events
from .EVENTS.WINDOW                import window_move_events
from .EVENTS.GUI_SELECT            import select_text, render_selection, build_selection
from .EVENTS.GUI_NUMBERS           import numbers
from .ASSETS.GUI_ASSETS            import create_assets
from .ASSETS.BUILD_SEARCH_BUTTONS  import rebuild_search
from .ASSETS.GUI_VARIABLES         import create_gui_variables
from .Editor.SHARED                import Col
from .Editor.Cath_Editor           import PyEdit_no_gui
from .Editor.Cath_Editor_Extras    import update_text_info
from .Editor.SHARED                import clear_selected, update_scroll_info, Col, save_timer
from pygame_gui.ui_manager         import UIManager
from pygame_gui.elements.ui_window import UIWindow
from pygame_gui.elements.ui_image  import UIImage


class Cath(pygame_gui.elements.UIWindow):
    
    
    def __init__(self, position, ui_manager):
        
        super().__init__(pygame.Rect(position, (800, 600)), ui_manager,
                         window_display_title='EDITOR!',
                         object_id='#window', resizable=True)
        
        surface_size = self.get_container().get_size()
        self.surface_element = UIImage(
            pygame.Rect((0, 0), surface_size),
            pygame.Surface(surface_size).convert(),
            manager=ui_manager,
            container=self,
            parent_element=self,
        )
        
        self.background       = pygame.Surface(surface_size)
        self.background       = self.background.convert()
        self.background.fill((0, 0, 0))
        self.parent           = self
        self.now              = 0
        
        self.app_path = os.path.dirname(os.path.abspath(__file__))
        print('Current Path:', self.app_path)
        
        create_gui_variables(self, position)
        create_assets(self, ui_manager)
        
        self.CATH = PyEdit_no_gui(self.EditorX, self.EditorY, self.Ewidth, self.Eheight,
                                  self.FPS, self.FONT, self.text_size, "white", self.parent)
        
    def process_event(self, event):
        super().process_event(event)
        
        self.CATH.update(event) # Backend Editor
        top_panel_buttons(self, event, self.ui_manager)
        bottom_panel_buttons(self, event, self.ui_manager)
        close_window(self, event, self.ui_manager)
        confirmation(self, event, self.ui_manager)
        window_close_events(self, event)
        text_entry(self, event)
        search_buttons(self, event)
        option_buttons(self, event, self.ui_manager)
        window_move_events(self, event)
        update_events_mouse(self, event)

    def update(self, time_delta):
        super().update(time_delta)
        save_timer(self, time_delta)
        x, y = pygame.mouse.get_pos()
        status_update(self, x, y)
        # Update Selection box
        if self.selecting == 1:
            build_selection(self)
        update_Vscroll(self)
        update_Hscroll(self)
        update_window_size(self)
        
        self.surface_element.image.blit(self.background, (0, 0))
        if self.selecting == 1:
            render_selection(self, self.surface_element.image)
        self.CATH.draw(self.surface_element.image)
        
        # Update Scroll Bars
        self.H_scroll_bg.draw(self.surface_element.image)
        self.V_scroll_bg.draw(self.surface_element.image)
        render_Vscroll(self, self.surface_element.image)
        render_Hscroll(self, self.surface_element.image)
        select_text(self)
        
        # Numbers Display
        numbers(self, self.surface_element.image)
        
    
