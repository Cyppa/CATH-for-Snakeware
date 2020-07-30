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

### Methods for text selection

from ..Editor.SHARED import clear_selected
from ..Editor.Cath_Editor_Extras import update_text_info

# Copy and paste
def copy_paste(self, which):
    
    if which == "copy":
        
        self.parent.top_label.set_text("TEXT COPIED")
        # If start  and end points are backwards then swap...
        if self.parent.sel_start[1] > self.parent.sel_end[1]:
            self.parent.sel_start, self.parent.sel_end = self.parent.sel_end, self.parent.sel_start 
        
        startX = self.parent.sel_start[0]
        endX   = self.parent.sel_end[0]
        startY = self.parent.sel_start[1] - 1
        endY   = self.parent.sel_end[1]
        
        # If selection is more than 1 line
        if startY + 1 != endY:
            # Get only the selected text from top and end lines
            line_start = self.lines[startY][startX:]
            line_end   = self.lines[endY -1][:endX]
            
            # Put top line into cache
            self.selected_text.append(line_start)
            # Put remaining selected lines into cache except the end line
            for l in range(startY + 1, endY - 1):
                self.selected_text.append(self.lines[l])
            # Put end line into cache    
            self.selected_text.append(line_end)
            
        # Else if selected text is on one line
        else:
            # If start  and end points are backwards then swap...
            
            if self.parent.sel_start[0] > self.parent.sel_end[0]:
                startX, endX = endX, startX
                
            line = self.lines[startY][startX:endX] # Slice string
            self.selected_text.append(line)        # Put into cache
        
    elif which == "paste":
        self.parent.top_label.set_text("PASTE")
        
        # If some text is selected, remove it first
        if self.parent.selected == 1: remove(self)
        
        # Split line at current cursor point
        before = self.lines[self.current_line - 1][:self.pos]
        after  = self.lines[self.current_line - 1][self.pos:]
        
        # If we are pasting just one line of text
        if len(self.selected_text) == 1:
            new_line                                        = before + self.selected_text[0] + after
            self.lines[self.current_line-1]                 = new_line
            # Update Cursor position
            self.pos         = self.pos + len(self.selected_text[0])
            self.display_pos = self.display_pos + len(self.selected_text[0])
        # If we are pasting multiple lines of text
        else:
            # Add top cached line to current cursor point
            new_line_top = before + self.selected_text[0]
            # Add bottom cached line to end of current cursor point
            new_bottom_line = self.selected_text[-1] + after
            # Create new top line
            self.lines[self.current_line - 1] = new_line_top
            # Insert body of selected text if more than top and bottom lines
            if len(self.selected_text) > 1:
                for i in range(1, len(self.selected_text) - 1):
                    self.lines.insert((self.current_line - 1) + i, self.selected_text[i])
                # Insert new bottom line(current line) + (length of cache - 1)
                self.lines.insert((self.current_line - 1) + (len(self.selected_text) - 1), new_bottom_line)            
   
        clear_selected(self)
        update_text_info(self)
        
        ### todo - leave cursor at end of pasted material!
        ### by using goto feature?

# Cutting Text
def cut(self):
    print("START: ", self.parent.sel_start, " END: ", self.parent.sel_end)
    # Make some swaps if selection was made 'backwards / upwards'
    if self.parent.sel_start[1] > self.parent.sel_end[1]:
        self.parent.sel_start[1], self.parent.sel_end[1] = self.parent.sel_end[1], self.parent.sel_start[1]
    if self.parent.sel_start[0] > self.parent.sel_end[0]:
        self.parent.sel_start[0], self.parent.sel_end[0] = self.parent.sel_end[0], self.parent.sel_start[0]
        
    startX = self.parent.sel_start[0]
    endX   = self.parent.sel_end[0]
    startY = self.parent.sel_start[1] - 1
    endY   = self.parent.sel_end[1]   - 1
    
    # Get text before selected text on starting line and text after selected text on end line
    before = self.lines[startY][:startX]
    after  = self.lines[endY][endX:]
    
    # Remove all lines between start and end of selection if more than 1 line long
    if startY != endY:
        
        # Put start & end together
        self.lines[startY] = before + after
        
        del self.lines[startY + 1:endY + 1]
        
        update_text_info(self)
        
    else:
        
        new_line = before + after
        self.lines[self.current_line -1 ] = new_line
        update_text_info(self)
        

def remove(self):
    cut(self)
    clear_selected(self)
    self.parent.selected  = 0
    self.parent.selecting = 0
    #self.pos -= 1
    update_text_info(self)
