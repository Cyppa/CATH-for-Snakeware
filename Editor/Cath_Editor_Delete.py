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

from ..Editor.Cath_Editor_Extras import update_text_info
from ..Editor.Cath_Editor_Select import remove

# Delete Key
def delete(self):
    # If there's a selection just clear that selection
    if self.parent.selected == 1: remove(self)
        
    # Otherwise act as normal
    else:
        
        update_text_info(self)
        
        # While there's text in the line
        if self.chars > 0:
            self.lines[self.i] = self.before + self.after[1:]
            self.current_text  = self.lines[self.i]
            
        # Or while cursor is at end of line and we are not on the last line
        if self.display_pos == self.chars and self.current_line < (len(self.lines) - 1):
            
            next_line_text    = self.lines[self.i + 1]       # Get the text of the next line
            self.current_text = self.before + next_line_text # Add it to remaining text of current line
            self.lines[self.i]=self.current_text             # Update the current line
            
            for l in range(len(self.lines)):                 # For any line lower
                if l > self.i and l < (len(self.lines) - 1): # Move the line up one
                    self.lines[l] = self.lines[l + 1]
            
            # Get the difference between real and displayed lines
            difference        = self.total_lines - self.display_current_line + 1
            difference_length = self.display_current_line + difference            
            """
            # Update displayed lines with real lines
            for l in range(self.display_current_line, difference_length):
                try:
                    self.display_lines[l - 1] = self.lines[l -1 + self.real]
                except IndexError:
                    self.lines.pop()
                    
                    if len(self.lines) < self.max_lines:
                        self.max_lines   = len(self.lines) -1
                        self.total_lines = len(self.lines) -1
                    break
            """
            # Remove last line of main list        
            self.lines.pop()
        # Remove any DEL formatting character       
        update_text_info(self)
