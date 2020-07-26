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
        
        startY = self.start[1] - 1 + self.real
        endY   = self.end[1]   + self.real
        startX = self.start[0] + 1
        endX   = self.end[0]   + 1
        
        # If selection is more than 1 line
        if self.start[1] != self.end[1]:
            
            # Get selected text from top and end lines
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
            line = self.lines[startY][startX:endX] # Slice string
            self.selected_text.append(line)        # Put into cache
        
        self.Extra_label.set_text("TEXT COPIED")
        
        with open("./cache.txt", 'a') as cache:
            print("[[", file = cache)
            for line in self.selected_text:
                print(line, file = cache)
            print("]]", file = cache)
        
    elif which == "paste":
        
        if self.show_clip == 0:
            # Get the lastest entry from history cache
            length      = len(self.start_end)
            self.cacheX = length
            if length > 0: self.cacheX = (self.cacheX - 1) % length
            
            for r in range(self.start_end[self.cacheX][0],self.start_end[self.cacheX][1] + 1):
                self.cached_list.append(self.cache[r].replace("\n", ""))
        
        # If some text is selected, remove it first
        if self.selected == 1: remove(self, self)
        
        # Split line at current cursor point
        before = self.lines[self.current_line - 1][:self.pos]
        after  = self.lines[self.current_line - 1][self.pos:]
        
        # If we are pasting just one line of text
        if len(self.cached_list) == 1:
            new_line                                        = before + self.cached_list[0] + after
            self.lines[self.current_line-1]                 = new_line
            self.display_lines[self.display_current_line-1] = new_line
            # Update Cursor position
            self.pos         = self.pos + len(self.cached_list[0])
            self.display_pos = self.display_pos + len(self.cached_list[0])
        # If we are pasting multiple lines of text
        else:
            # Add top cached line to current cursor point
            new_line_top = before + self.cached_list[0]
            # Add bottom cached line to end of current cursor point
            new_bottom_line = self.cached_list[-1] + after
            # Create new top line
            self.lines[self.current_line - 1] = new_line_top
            
            # Insert body of selected text if more than top and bottom lines
            if len(self.cached_list) > 1:
                for i in range(1, len(self.cached_list) - 1):
                    self.lines.insert((self.current_line - 1) + i, self.cached_list[i])
                # Insert new bottom line(current line) + (length of cache - 1)
                self.lines.insert((self.current_line - 1) + (len(self.cached_list) - 1), new_bottom_line)            
            
            # Get range of lines to input into display
            if len(self.lines) > len(self.display_lines) and len(self.lines) < self.max_lines:
                rang = len(self.lines)
            else: rang = self.max_lines
            
            self.display_lines.clear()
            
            # Get the id's of displayed lines to alter
            diff = self.current_line - self.display_current_line
            
            # Update displayed screen/ text
            for i in range(rang):
                self.display_lines.append("")
                self.display_lines[i] = self.lines[i + diff]
                
        clear_selected(self)
        update_text_info(self)
        self.update_display(0)
        ### todo - leave cursor at end of pasted material!
        ### by using goto feature?
   
# Selected Text
def select(self, start, end):
    
    update_text_info(self)
    
    self.start[0] = start[0]
    self.start[1] = start[1]
    self.end[0]   = end[0]
    self.end[1]   = end[1]
    
    # If text was selected 'backwards' swap start and end positions
    if self.start[0] > self.end[0]:
        
        self.start[0], self.end[0] = self.end[0], self.start[0]
   
    # Select on one line
    if start[1] == end[1]:
        # If selecting text while line is scrolled because line is longer than max character length
        self.start[0] = start[0]
        self.end[0]   = end[0]
    
    self.start[0] = self.start[0]
    
    self.start[1] = start[1] + self.real
    self.end[1]   = end[1]   + self.real
    
    if self.upwards == 1:
        self.start[0] = self.start[0] - 1
        self.upwards = 0
    else: self.start[0] = self.start[0]
            
    self.pos                  = self.start[0] + 1
    self.display_pos          = self.start[0] + 1
    self.current_line         = self.start[1]
    self.display_current_line = self.start[1] - self.real
    print('self.new_pos', self.new_pos)
    
    if start != end:
        self.selected = 1

# Cutting Text
def cut(self, start, end):
    
    startX = start[0] + 1
    startY = start[1] - 1
    endX   = end[0] + 1
    endY   = end[1] - 1
    
    # Get text before selected text on starting line and text after selected text on end line
    before = self.lines[startY][:startX]
    after  = self.lines[endY][endX:]
    
    # Remove all lines between start and end of selection if more than 1 line long
    if start[1] != end[1]:
        
        # Put start & end together
        self.lines[startY] = before + after
        self.display_lines[startY - self.real] = self.lines[startY]
        
        del self.lines[startY + 1:endY + 1]

        # Update display
        self.display_lines.clear()
        if len(self.lines) < self.max_lines:
            rang = len(self.lines)
        else:
            rang = self.max_lines - 1
    
        for l in range(rang):
            self.display_lines.append("")
            self.display_lines[l] = self.lines[l + self.real]
        update_text_info(self)
        
    else:
        new_line = before + after
        self.lines[self.current_line -1 ] = new_line
        self.display_lines[self.display_current_line - 1] = new_line
        update_text_info(self)
        

def remove(self):
    cut(self, self.start, self.end)
    clear_selected(self)
    self.selected = 0
    #self.pos -= 1
    update_text_info(self)
