import pygame

from ..Editor.Cath_Editor_Extras import update_text_info
from ..Editor.SHARED import clear_selected, Col

def select_text(self):
    
    surface = self.surface_element.image
    
    # If mouse is pressed down lets get/ create some vars
    # needed for selecting text
    if (
        self.mouse == 1 and self.sel_loop == 0    and
        (self.mouse_X) < self.CATH.max_line_chars and
        (self.mouse_Y) < self.CATH.total_lines +1 and
        self.H_scr_grabbed == 0 and
        self.V_scr_grabbed == 0 and
        self.window_move   == False and
        self.should_use_window_edge_resize_cursor() == False
        ):
        
        pos                = self.line_len - self.CATH.new_pos
        if pos < 0: pos    = 0
        self.grab_line_len = len(self.CATH.lines[self.mouse_Y - 1 + self.CATH.real])
        self.sel_start     = [self.mouse_X + self.CATH.new_pos - 1, self.mouse_Y + self.CATH.real]
        self.sel_loop      = 1
        
        if self.sel_start[0] > self.grab_line_len:
            self.sel_start[0] = self.grab_line_len
            
    # Check if we are selecting text
    # Is mouse pressed? Has mouse position changed since it's been pressed?
    if (
        self.mouse == 1 and self.sel_loop == 1 and 
        (self.sel_start[0] != self.mouse_X or
         self.sel_start[1] != self.mouse_Y) and
        self.V_scr_grabbed == 0 and
        self.H_scr_grabbed == 0 and
        self.window_move   == False and
        self.should_use_window_edge_resize_cursor() == False
        ):
        
        if self.mouse_Y + self.CATH.real < len(self.CATH.lines):
            
            self.sel_end = [self.mouse_X + self.CATH.new_pos, self.mouse_Y + self.CATH.real]
            self.release_line_len = len(self.CATH.lines[self.sel_end[1] - 1])
            
            if self.sel_end[0] > self.release_line_len:
                self.sel_end[0] = self.release_line_len
            
            self.selecting = 1
            self.no_scroll = 1
        
        def select_scroll(self, direction):
            
            if direction == "down" or "up"   : speed = self.sel_move_line_speed                
            if direction == "left" or "right": speed = self.sel_move_char_speed 
            # Start counter
            self.sel_count += 1
            # If counter reaches moving time activate moving speed counter
            if self.sel_count > 10:
                move = self.sel_count % speed
                # move speed counter has done one cycle: scroll text
                if move == 0:
                    # Scroll display
                    if direction == "down" : self.CATH.real += 1
                    if direction == "up"   : self.CATH.real -= 1
                    if direction == "left" : self.CATH.new_pos -= 1
                    if direction == "right": self.CATH.new_pos += 1
                    
        # Has selection hit bottom line?
        if (self.mouse_Y == self.CATH.max_lines - 1 and
            self.selecting == 1 and
            self.CATH.real < len(self.CATH.lines) - 1 - self.CATH.max_lines):
            select_scroll(self, "down")
                    
        # Has selection hit top line?
        if (self.mouse_Y   <= 1 and
            self.selecting == 1 and
            self.CATH.real > 0):
          select_scroll(self, "up")
                    
        # Has selection hit right of line?
        if (self.mouse_X >= self.CATH.max_line_chars and
            self.selecting == 1):
            select_scroll(self, "right")
                    
        # Has selection hit left of line?
        if (self.mouse_X < 1 and self.CATH.new_pos > 0 and
            self.selecting == 1):
            select_scroll(self, "left")
                        
def build_selection(self):
    #self.top_label.set_text('Selecting')
    start    = [0, 0]
    end      = [0, 0]
    start[0] = self.sel_start[0] - self.CATH.new_pos
    start[1] = self.sel_start[1] - self.CATH.real - 1
    end[0]   = self.sel_end[0]   - self.CATH.new_pos
    end[1]   = self.sel_end[1]   - self.CATH.real - 1
    # Fix offset if line numbers are displayed or not
    if self.numbers == 1:
        EditorX = self.EditorX + self.offset
    else: EditorX = self.EditorX_old
    # If we only need one line
    if start[1] == end[1]:
        # Top Line
        self.selX1 = (start[0] * self.CATH.text_width) + EditorX
        self.selY1 = (start[1] * self.CATH.text_size)  + self.EditorY
        self.selX2 = ((end[0] - start[0])  * self.CATH.text_width) + self.offset
        self.selY2 = self.CATH.text_size
        # Clear bottom line
        self.selX1a, self.selY1a = 0, 0
        self.selX2a, self.selY2a = 0, 0
        # Cl3ar Body / Lines of Selected Text
        self.bX1,    self.bY1    = 0, 0
        self.bX2,    self.bY2    = 0, 0
    # 2  or more Lines
    elif ((start[1] < end[1]) or (start[1] > end[1])):
        # If selecting upwards swap start and end
        if (start[1] >= end[1] + 1):
                start, end = end, start
        # Top Line
        pos = (start[0] * self.CATH.text_width) + EditorX
        self.selX1 = pos
        self.selY1 = (start[1] * self.CATH.text_size)  + self.EditorY
        self.selX2 = (self.CATH.max_line_chars * self.CATH.text_width) - pos + EditorX
        self.selY2 = self.CATH.text_size
        # Bottom Line
        self.selX1a = EditorX
        self.selY1a = (end[1] * self.CATH.text_size)  + self.EditorY
        self.selX2a = ((end[0]) * self.CATH.text_width)
        self.selY2a = self.CATH.text_size
        if (start[1] == end[1] + 1) or (start[1] == end[1] - 1):
            # Clear Body / Lines of Selected Text
            self.bX1,    self.bY1    = 0, 0
            self.bX2,    self.bY2    = 0, 0
        # If selecting more than 2 lines upwards swap start and end
        else:
            # We need total lines minus top and bottom lines
            line_amount = end[1] - start[1] - 1
            self.bX1    = EditorX
            self.bY1    = ((start[1] + 1) * self.CATH.text_size)  + self.EditorY
            self.bX2    = self.CATH.max_line_chars * self.CATH.text_width
            self.bY2    = self.CATH.text_size * line_amount
        
# draw selection box        
def render_selection(self, surface):
    # Stop rendering if outside of visible area
    if self.selY1 > (self.EditorY - self.CATH.text_size):
        # Top line
        pygame.draw.rect(surface,Col("grey", 50),
                        (self.selX1, self.selY1, self.selX2, self.selY2))
    if self.selY1a > (self.EditorY - self.CATH.text_size):    
        # Bottom line
        pygame.draw.rect(surface,Col("grey", 50),
                        (self.selX1a, self.selY1a, self.selX2a, self.selY2a))
        
        # Selection Body lines
        pygame.draw.rect(surface,Col("grey", 50),
                        (self.bX1, self.bY1, self.bX2, self.bY2))
        