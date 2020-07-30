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

# Backspace
def backspace(self):
    
    update_text_info(self)
    self.rock_bottom = 0
    
    # If there's a selection just clear that selection
    if self.parent.selected == 1: remove(self)
    
    # Otherwise act as normal
    else:            
        # Find out if amount of lines in file list is the same as amount able to be displayed...
        if len(self.lines) == self.total_lines:
            self.only_display = 1
            
        # Find out where last Line of 'file list' is...
        self.bottom         = len(self.lines) - 1
        self.display_bottom = self.total_lines
        
        # Find out if we have hit rock bottom on screen
        if self.display_bottom + self.real == self.bottom:
            self.rock_bottom = 1
        
        # If cursor is at the start of a line but not on the first line
        if self.pos < 1 and self.current_line > 1:
            
            txt = self.lines[self.current_line]
            self.after = self.lines[self.i]                     # Get the entire line of text
            self.i -= 1 
            self.current_line = self.i + 1                   
            self.current_text = self.lines[self.i]              # Get the length of line above
            self.pos = len(self.current_text)                   # Place cursor at end of that line
            self.lines[self.i] = self.current_text + self.after # Join lines together
            if len(self.current_text) > self.CATH.max_line_chars:
                self.CATH.new_pos = len(self.current_text) - self.CATH.max_line_chars
            for l in range(len(self.lines)):                    # For any line lower
                if l > self.i and l < (len(self.lines) - 1):    # Move the line up one
                    self.lines[l] = self.lines[l + 1]           
            
            # Update displayed lines with real lines
            # If bottom line of text has not showed up yet take away lines from bottom of file
            if self.rock_bottom == 0 and self.only_display == 0:
                
                # Range from current displayed line to end
                self.display_current_line -= 1
                # Remove last line of main list
                self.lines.pop()
                
            # Otherwise take lines away from top of file by bringing them down one spot
            elif self.rock_bottom == 1 and self.only_display == 0:
                
                # Range from beginning of file list to current displayed line
                # Reverse the iteration and move all lines up one spot                    
                for h in range(self.current_line, -1, -1):
                    self.lines[h] = self.lines[h - 1]
                
                # Insert current text back into file list at current line
                self.lines.insert(self.current_line + 1, txt)
                
                # Remove excess line from bottom of file list becasue we added current line before
                self.lines.pop()
                # Remove top line which is now empty
                self.lines.pop(0)
            
            else:
                
                self.display_current_line = self.current_line
                self.lines.pop()
            
            # Update amount of total_lines
            if len(self.lines) == self.total_lines:
                self.total_lines -= 1
            if len(self.lines) < self.max_lines:
                self.total_lines = len(self.lines) -1
            update_text_info(self)
        
        # If cursor is not at the start of line
        elif self.pos > 0:
            self.current_text  = self.lines[self.i]              # Get the line of text
            self.after         = self.current_text[self.pos:]    # Get text after cursor position
            self.before        = self.current_text[:self.pos - 1]# Get text before cursor position less 1
            self.lines[self.i] = self.before + self.after        # Join before and after to create line without deleted character
            self.pos -= 1                                        # Move cursor back a space
            
        update_text_info(self)
        self.back_space = 1
        
        # Do we need to scroll back?
        if self.current_line + self.real - 1 == len(self.lines):
            print('bottom')
        current_line_len = len(self.lines[self.current_line - 1])
        if current_line_len > self.max_line_chars:
            self.new_pos -= 1
