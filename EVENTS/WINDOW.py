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

import pygame, pygame_gui
from ..EVENTS.GUI_METHODS import update_bg
from ..Editor.SQUARE      import Square

### From Main File
def window_move_events(self, event):
    pass
    
    if event.type == pygame.USEREVENT and event.user_type == 'window_selected':
        event.ui_element.is_active = True
        print('you have selected window')
    """
    # If mouse is over title bar set a variable to help with winodw coords/ resizing                
    if(event.type         == pygame.USEREVENT and
       event.user_type    == pygame_gui.UI_BUTTON_ON_HOVERED and
       event.ui_object_id == "#window.#title_bar" and
       event.ui_element   == self.title_bar):
        print('over bar')
        self.window_move = True
    
    if(event.type         == pygame.USEREVENT and
       event.user_type    == pygame_gui.UI_BUTTON_ON_UNHOVERED and
       event.ui_object_id == "#window.#title_bar" and
       event.ui_element   == self.title_bar):
        print('under bar')
        self.window_move = False
    """
    if(event.type         == pygame.USEREVENT and
       event.user_type    == pygame_gui.UI_BUTTON_PRESSED and
       event.ui_object_id == "#window.#title_bar" and
       event.ui_element   == self.title_bar):
        print('we are the...', pygame.mouse.get_pos())
        self.window_move = True
        
        print('MOVING')
        # Some variables to help update window size and position
        # This enables us to get relative mouse position inside text window
        
        self.win_grab           = self.get_container().get_size()
        self.GRAB               = pygame.mouse.get_pos()         
        self.mouse              = 1
        
    if event.type == pygame.MOUSEBUTTONUP and self.window_move == True:
        self.window_move = False # reset var
        print('have we moved window')
        # A method to get relative mouse coords inside text window... #
        win_size = self.get_container().get_size()
        x, y = pygame.mouse.get_pos()
        
        if win_size[0] > self.win_grab[0]:
            if x < self.GRAB[0]: self.rel_X -= (x - self.GRAB[0])

        if win_size[0] < self.win_grab[0]:
            if x > self.GRAB[0]: self.rel_X -= (x - self.GRAB[0])
        
        if win_size[1] > self.win_grab[1]:
            if y < self.GRAB[1]: self.rel_Y -= (y - self.GRAB[1])
        
        if win_size[1] < self.win_grab[1]:
            if y > self.GRAB[1]: self.rel_Y -= (y - self.GRAB[1])
                
        if x < self.GRAB[0] and win_size == self.win_grab:
            self.rel_X = self.GRAB[0] - x + self.rel_X
        elif x > self.GRAB[0] and win_size == self.win_grab:
            self.rel_X = self.GRAB[0] - x + self.rel_X
            
        if y < self.GRAB[1] and win_size == self.win_grab:
            self.rel_Y = self.GRAB[1] - y + self.rel_Y
        elif y > self.GRAB[1] and win_size == self.win_grab:
            self.rel_Y = self.GRAB[1] - y + self.rel_Y
        # End method to get relative mouse coords inside text window #
        
        self.mouse             = 0 # Tell certain modules we have released mouse
    
### From main(self).Editor
def update_window_size(self):
    
    # Keep Window size updated
    self.surface_size     = self.get_container().get_size()
    self.panel_W          = self.surface_size[0]
        
    # Adjust labels' text to resizing
    self.label_W          = self.panel_W - (self.offset * 2) - (self.buttonX * 2)
    self.stat_label_chars = self.label_W // self.text_width
    self.top_label_chars  = ((self.panel_W - (5 * self.buttonX)) // self.text_width) - 2
    if self.top_label_chars < 0 : self.top_label_chars  = 0
    if self.stat_label_chars < 0: self.stat_label_chars = 0
    
    #Check if window dimensions have change, if so rebuild assets
    if self.prev_sizeX != self.surface_size[0]:
        self.top_label.set_text("")
        self.prev_sizeX = self.surface_size[0]
        
        # Update Vertical Scroll bar position
        self.V_scroll_X  = self.surface_size[0] - self.scroll_W
        
        if self.search_button_pressed == True:
            self.text_entryX  = round((self.panel_W - (self.buttonX * 2.5))/ 2) - 4
            rebuild_search(self, self.ui_manager, self.text_entryX)
        
        # Update size of window background
        if self.surface_element: self.surface_element.kill()
        update_bg(self, self.surface_size, self.ui_manager)
        
        # Update CATH width
        self.CATH.max_line_chars = round(self.panel_W / self.CATH.text_width) - 3
        print('Max Line Characters:', self.CATH.max_line_chars, 'new=pos', self.CATH.new_pos)
        
        # Update Scroll Bars
        self.V_scroll_bg = Square(self.surface_element.image, self.V_scroll_X - 2, self.V_scroll_Y - 2,
                                 self.scroll_W + 1, self.surface_size[1] - self.V_scroll_Y + 1,
                                 orient = "vertical", colour = "grey", fill = True, line_width = 1)
        
        self.H_scroll_bg = Square(self.surface_element.image, self.EditorX - 2, self.surface_size[1] - self.scroll_W - 2,
                                 self.scroll_W + 1, self.surface_size[0] - self.scroll_W - 2,
                                 orient = "horizontal", colour = "grey", fill = True, line_width = 1)
        
    if self.prev_sizeY != self.surface_size[1]:
        # Update CATH height
        self.CATH.max_lines = round((self.surface_size[1] - self.EditorY)/ self.CATH.text_size) - 2
        
        if self.prev_sizeY < self.surface_size[1]:
            ## Find out if bottom line has appeared on screen...
            ## NEEDS SERIOUS WORK! IS NOT WORKING YET...
            print('GROWING')  
        else:
            print('SHRINKING')
        self.CATH.update_max_lines()
        
        self.prev_sizeY     = self.surface_size[1]
        
        if self.surface_element: self.surface_element.kill()
        update_bg(self, self.surface_size, self.ui_manager)
        
        # Update Scroll Bars
        self.V_scroll_bg = Square(self.surface_element.image, self.V_scroll_X - 2, self.V_scroll_Y - 2,
                                 self.scroll_W + 1, self.surface_size[1] - self.V_scroll_Y + 1,
                                 orient = "vertical", colour = "grey", fill = True, line_width = 1)
        
        self.H_scroll_bg = Square(self.surface_element.image, self.EditorX - 2, self.surface_size[1] - self.scroll_W - 2,
                                 self.scroll_W + 1, self.surface_size[0] - self.scroll_W - 2,
                                 orient = "horizontal", colour = "grey", fill = True, line_width = 1)
