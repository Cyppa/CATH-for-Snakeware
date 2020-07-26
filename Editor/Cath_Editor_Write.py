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
            
            if self.selected == 1:
                cut(self, self.start, self.end)
                clear_selected(self)
                
            self.selected      = 0
            self.selected = 0
            
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
            self.display_lines[self.display_current_line - 1] = self.current_text
            
            #if self.pos > self.max_line_chars: self.new_pos += 1
            # Horizontal scrolling offset
            if self.pos >= self.max_line_chars + self.new_pos:
                self.new_pos += 1
        """
        # CTRL / ALT, etc combos
        elif self.ctrl == 1:
            
            if self.selected == 1:
                # Key 'C' Copy
                if key == 99:
                    self.selected_text.clear()
                    copy_paste(self, "copy", self)
                    self.cacheX = 0
                
                # Key 'X' Cut
                if key == 120:
                    self.selected_text.clear()
                    copy_paste(self, "copy", self)
                    remove(self, self)
                    
            # Key 'V' Paste
            if key == 118:
                
                self.start_point.clear()
                self.end_point.clear()
                self.cached_list.clear()
                self.start_end.clear

                self.paste       = 1
                self.cached_line = ""
                self.cache       = open("./Editor/cache.txt", 'r').readlines()

                # Search through history cache file, each entry is separated by the lines '[[' and ']]'
                for l in range(len(self.cache)):
                    if "[" == self.cache[l][0] and "[" == self.cache[l][1] and "\n" == self.cache[l][2]:
                        self.start_point.append(l + 1)
                    if "]" == self.cache[l][0] and "]" == self.cache[l][1] and "\n" == self.cache[l][2]:
                        self.end_point.append(l - 1)

                # Create a list of individual histroy entry start and end point
                for l in range(len(self.start_point)):
                    self.start_end.append([self.start_point[l], self.end_point[l]])
        """
