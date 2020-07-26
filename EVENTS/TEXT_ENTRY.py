import pygame
import pygame_gui

from ..Editor.SHARED             import GOTO_line
from ..Editor.Cath_Editor_Search import search_text, replace_text
from pygame_gui.elements       import UITextEntryLine


# Text Entry Change
def text_entry(self, event):
    
    if (event.type == pygame.USEREVENT and
        event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED):
        
        # Text Entry Search
        if event.ui_element == self.text_entry_search:
            self.search_string = event.text
            self.top_label.set_text("")
            self.CATH.search = 1
            self.re_search == 1
            
        # Text Entry Replace
        if event.ui_element == self.text_entry_replace:
            self.replace_string = event.text
            self.top_label.set_text("")
            self.CATH.search = 1
            self.re_search == 1
            
        # Text Entry Goto
        if event.ui_element == self.text_entry_goto:
            self.goto_string = event.text
            
    # Text Entry Finish
    if (event.type == pygame.USEREVENT and
        event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED):
        
        # Search
        if event.ui_element == self.text_entry_search:
            self.search_string = event.text
            search_text(self, self.search_string, "down")
            self.CATH.search = 1
            self.CATH.cursor_length = len(self.search_string)
            self.re_search == 1
        
        # Replace
        if event.ui_element == self.text_entry_replace:
            self.replace_string = event.text
            replace_text(self, self.replace_string, "once")
            self.CATH.search = 1
            self.CATH.cursor_length = len(self.search_string)
            self.re_search == 1
        
        # Text Entry Goto
        if event.ui_element == self.text_entry_goto:
            self.goto_string = event.text
            
            try:
                integer = int(self.goto_string)
                GOTO_line(self, integer)
            except ValueError: self.top_label.set_text(("INVALID INPUT!")[:self.top_label_chars])
            else: pass
