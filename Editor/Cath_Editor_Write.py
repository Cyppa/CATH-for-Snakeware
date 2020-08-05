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

from ..Editor.SHARED             import clear_selected
from ..Editor.Cath_Editor_Extras import update_text_info, write_area
from ..Editor.Cath_Editor_Select import copy_paste, cut, remove

# WRITING / Display charatcers to screen
def write(self, key):
    
    for item in self.ignore_keys:
        if self.no_entry == 0 and key == item: self.ignore = 1 
    
    if self.ignore == 0 and self.no_entry == 0:  # Here we can add to a list of keys to ignore          
        
        write_area(self)
                
        if self.ctrl == 0 and self.alt == 0 and self.super == 0 and self.arrow == 0:
            
            update_text_info(self)
            
            if self.parent.selected == 1:
                cut(self)
                clear_selected(self)
                
            self.parent.selected  = 0
            self.parent.selecting = 0
            
            def display(key, upper = 0):
                
                if upper == 0: _X_ = chr(key)
                else: _X_ = chr(key).upper()
                
                if self.insert == 0:
                    self.current_text = self.before + _X_ + self.after
                else:
                    self.current_text = self.before + _X_ + self.after[1:] # Overwrite/ Insert
            
            if self.Lshift == 1 or self.Rshift == 1: # Upper Case Shift keys
                for K in self.special:
                    if self.no_entry == 0 and key == K[0]: key = K[1]
                display(key, upper = 1)
            elif self.caps == 1: display(key, upper = 1) # Caps
            else: display(key, upper = 0)                # Lower case
            
            # Editor Box Text
            self.pos += 1
            self.lines[self.i] = self.current_text
            update_text_info(self)
            
            # Horizontal scrolling offset
            if self.pos >= self.max_line_chars + self.new_pos:
                self.new_pos += 1
        
        # CTRL / ALT, etc combos
        elif self.ctrl == 1:
            
            if self.parent.selected == 1:
                # Key 'C' Copy
                if key == 99:
                    self.selected_text.clear()
                    copy_paste(self, "copy")
                    self.cacheX = 0
                    
                # Key 'X' Cut
                if key == 120:
                    self.selected_text.clear()
                    copy_paste(self, "copy")
                    remove(self)
                    
            # Key 'V' Paste
            if key == 118:
                if len(self.selected_text) > 0:
                    copy_paste(self, "paste")   
                self.paste = 0