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

from ..Editor.SHARED import GOTO_line
from ..Editor.Cath_Editor_Extras import update_text_info


def replace_text(self, replace_string, amount):
    
    if self.not_found == 0:
            
        if amount == "all":
            for l in range(len(self.CATH.lines)):
                if self.search_string in self.CATH.lines[l]:
                    self.CATH.lines[l] = self.CATH.lines[l].replace(self.search_string, replace_string)
        # Remeber make 'number' dynamic...
        if self.numbers == 1:
            number = 4
        else: number = 0
        
        for l in range(len(self.CATH.display_lines)-1):
            self.CATH.display_lines[l] = self.CATH.lines[l]
            
        self.CATH.update_display(number)
        
        if amount == "once":
            
            pos  = self.Occounter[self.occurance - 1][1]
            l    = list(self.CATH.display_lines[self.CATH.display_current_line - 1])
            lenn = len(self.search_string)
            
            del l[pos - 1:pos - 1 + lenn]
            l        = ",".join(l).replace(",", "")
            l_before = l[:pos - 1]
            l_after  = l[pos - 1:]
            l        = l_before + replace_string + l_after
            
            self.CATH.display_lines[self.CATH.display_current_line - 1] = l
            self.CATH.lines[self.CATH.current_line - 1] = l
        
        self.re_search = 1
    else: self.top_label.set_text(("NOT FOUND!")[:self.top_label_chars])
    
def search_text(self, search_string, direction):
    
    try:
        
        # If search string has changed, reset some variables
        if (search_string != self.previous_string) or self.re_search == 1 or self.CATH.re_search == 1:
            self.re_search  = 0
            self.occurance  = 0
            self.Occounter.clear()
            sear = []
            start_ = 0
            
            # Scan lines for text...
            for l in range(len(self.CATH.lines)):
                
                # Many of this next bit of code from: https://stackoverflow.com/questions/11476713/determining-how-many-times-a-substring-occurs-in-a-string-in-python    
                nStr    = self.CATH.lines[l]
                pattern = search_string
                count  = 0
                flag    = True
                start   = 0
                
                while flag:
                    a = nStr.find(pattern,start)  # find() returns -1 if the word is not found, 
                                                  #start i the starting index from the search starts(default value is 0)
                    if a == -1:                   #if pattern not found set flag to False
                        flag = False
                    else:                         # if word is found increase count and set starting index to a+1
                        count += 1        
                        start = a + 1
                        self.Occounter.append([l + 1, start])
                # End copy of code...
                
        if len(self.Occounter) != 0:
            if direction == "up":
                self.occurance = (self.occurance - 1) % len(self.Occounter)
            if direction == "down":
                self.occurance = (self.occurance + 1) % len(self.Occounter)
        
            # Update Cursor Position
            try:
                line                           = self.Occounter[self.occurance - 1][0]
                pos                            = self.Occounter[self.occurance - 1][1]
                
                GOTO_line(self, line)
                self.CATH.display_pos          = pos - 1 - self.CATH.new_pos
                self.CATH.pos                  = pos - 1
                
                # Is found text off screen to the left?
                if self.CATH.pos < self.CATH.new_pos:
                    x_amount = self.CATH.new_pos - self.CATH.pos
                    print('OFF SCREEN!! By', x_amount, 'characters...')
                    # Bring screen to text
                    self.CATH.new_pos -= x_amount
                    self.CATH.display_pos += x_amount
                
                # Is found text off screen to the right?   
                if self.CATH.pos > self.CATH.max_line_chars + self.CATH.new_pos:
                    x_amount = self.CATH.pos - self.CATH.max_line_chars + self.CATH.new_pos
                    print('OFF SCREEN RIGHT!! By', x_amount, 'characters...')
                    
                    self.CATH.new_pos += x_amount + len(search_string)
                    self.CATH.display_pos -= x_amount + len(search_string)
                    
                self.CATH.current_line         = line
                occur                          = self.occurance
                update_text_info(self.CATH)
                
                if self.occurance == 0: occur = len(self.Occounter)
                self.top_label.set_text(("FOUND: " + str(occur) + " / " +
                                          str(len(self.Occounter)))[:self.top_label_chars])
                print('self.top_label_chars', self.top_label_chars)
                
                if line > self.CATH.max_lines:
                    self.CATH.display_current_line = self.CATH.max_lines
                    
                else:
                    self.CATH.display_current_line = self.CATH.current_line

                self.previous_string = search_string
                self.not_found       = 0
                
            except TypeError: pass
        else:
            self.top_label.set_text(("NOT FOUND!")[:self.top_label_chars])
            self.not_found = 1
            print('Not Found', self.CATH.total_lines)
        
    except IndexError:
        self.top_label.set_text(("NOT FOUND!")[:self.top_label_chars])
        self.not_found = 1
        print("Not Found")
