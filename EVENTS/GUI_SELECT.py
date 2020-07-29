import pygame

from ..Editor.Cath_Editor_Extras import update_text_info
from ..Editor.SHARED import clear_selected, Col
from ..Editor.Cath_Editor_Select import select

def select_text(self):
    
    surface = self.surface_element.image
    width   = self.text_width
    
    # If mouse is pressed down lets get/ create some vars
    # needed for selecting text
    if (self.mouse == 1 and self.sel_loop == 0 and
        (self.mouse_X) < self.CATH.max_line_chars and
        (self.mouse_Y) < len(self.CATH.display_lines) - 1):
        
        pos                = self.line_len - self.CATH.new_pos
        if pos < 0: pos    = 0
        self.grab_line_len = len(self.CATH.lines[self.mouse_Y - 1 + self.CATH.real])
        self.sel_start     = [self.mouse_X + self.CATH.new_pos, self.mouse_Y + self.CATH.real]
        self.sel_loop      = 1
        
        if self.sel_start[0] > self.grab_line_len:
            self.sel_start[0] = self.grab_line_len
            
    # Check if we are selecting text
    # Is mouse pressed? Has mouse position changed since it's been pressed?
    if (
        self.mouse == 1 and self.sel_loop == 1 and 
        (self.sel_start[0] != self.mouse_X     or
         self.sel_start[1] != self.mouse_Y)    and
        self.V_scr_grabbed == 0                and
        self.H_scr_grabbed == 0
        ):
        
        self.sel_end = [self.mouse_X + self.CATH.new_pos, self.mouse_Y + self.CATH.real]
        self.release_line_len = len(self.CATH.lines[self.sel_end[1] - 1])
        
        if self.sel_end[0] > self.release_line_len:
            self.sel_end[0] = self.release_line_len
        
        self.selecting = 1
        self.no_scroll = 1
        
        # Has selection hit bottom line?
        if self.mouse_Y == self.CATH.max_lines - 1 and self.selecting == 1:

            # Start counter
            self.sel_count += 1
            
            # If counter reaches moving time activate moving speed counter
            if self.sel_count > 20:
                move = self.sel_count % self.sel_move_line
                
                # move speed counter has done one cycle: scroll text
                if move == 0:
                    
                    # Scroll display
                    self.CATH.real += 1
                    for l in range(len(self.CATH.display_lines)):
                        self.CATH.display_lines[l] = self.CATH.lines[l + self.CATH.real]
    
    #if self.mouse
                        
def build_selection(self):
    #self.top_label.set_text('Selecting')
    start    = [0, 0]
    end      = [0, 0]
    start[0] = self.sel_start[0] - self.CATH.new_pos
    start[1] = self.sel_start[1] - self.CATH.real - 1
    end[0]   = self.sel_end[0]   - self.CATH.new_pos
    end[1]   = self.sel_end[1]   - self.CATH.real - 1
    
    # If we only need one line
    if start[1] == end[1]:
        # Top Line
        self.selX1 = (start[0] * self.text_width) + self.EditorX
        self.selY1 = (start[1] * self.text_size)  + self.EditorY
        self.selX2 = ((end[0] - start[0])  * self.text_width) + self.EditorX
        self.selY2 = self.text_size
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
        pos = (start[0] * self.text_width) + self.EditorX
        self.selX1 = pos
        self.selY1 = (start[1] * self.text_size)  + self.EditorY
        self.selX2 = (self.CATH.max_line_chars * self.text_width) - pos + self.EditorX
        self.selY2 = self.text_size
        # Bottom Line
        self.selX1a = self.EditorX
        self.selY1a = (end[1] * self.text_size)  + self.EditorY
        self.selX2a = ((end[0]) * self.text_width)
        self.selY2a = self.text_size
        if (start[1] == end[1] + 1) or (start[1] == end[1] - 1):
            # Clear Body / Lines of Selected Text
            self.bX1,    self.bY1    = 0, 0
            self.bX2,    self.bY2    = 0, 0
        # If selecting more than 2 lines upwards swap start and end
        else:
            # We need total lines minus top and bottom lines
            line_amount = end[1] - start[1] - 1
            self.bX1    = self.EditorX
            self.bY1    = ((start[1] + 1) * self.text_size)  + self.EditorY
            self.bX2    = self.CATH.max_line_chars * self.text_width
            self.bY2    = self.text_size * line_amount
        
# draw selection box        
def render_selection(self, surface):
    # Stop rendering if outside of visible area
    if self.selY1 > (self.EditorY - self.text_size):
        # Top line
        pygame.draw.rect(surface,Col("grey", 50),
                        (self.selX1, self.selY1, self.selX2, self.selY2))
    if self.selY1a > (self.EditorY - self.text_size):    
        # Bottom line
        pygame.draw.rect(surface,Col("grey", 50),
                        (self.selX1a, self.selY1a, self.selX2a, self.selY2a))
        
        # Selection Body lines
        pygame.draw.rect(surface,Col("grey", 50),
                        (self.bX1, self.bY1, self.bX2, self.bY2))
        
        
def select_scroll(self):
    
    # Has selection hit bottom line?
    if self.mouse_Y == self.CATH.max_lines - 1:
        self.top_label.set_text("Bottom")# + str(self.sel_count))
        
        # Start counter
        self.sel_count += 1
        
        # If counter reaches moving time activate moving speed counter
        if self.sel_count > 20:
            move = self.sel_count % self.sel_move_line
            
            # move speed counter has done one cycle: scroll text
            if move == 0:
                
                # Scroll display
                self.CATH.real += 1
                for l in range(len(self.CATH.display_lines)):
                    self.CATH.display_lines[l] = self.CATH.lines[l + self.CATH.real]
                
                if self.selY1 > self.text_size:
                    self.top_label.set_text("SCROLL SEL" + str(self.selY1))
                    self.selY1 -= self.text_size
        
        
    """
    ## SELECTING
    O       = self.offset * 4
    Y       = self.EditorY
    Width   = self.text_width
    surface = self.surface_element.image    
    
    ## Cursor Select
    sX1, sY1, sX2, sY2 = self.sX1, self.sY1, self.sX2, self.sY2
    
    #sX1     = ((self.mouse_X - 1) * Width) + self.offset
    #sY1     = (self.mouse_Y * self.text_size) + Y
    #sX2     = Width
    #sY2     = self.text_size
    
    sX1     = (self.mouseX - Width) + self.offset
    sY1     = (self.mouseY) + Y
    sX2     = Width
    sY2     = self.text_size
    
    if self.select_cursor == 1:
        
        self.select = pygame.draw.rect(surface, (160, 160, 160), (sX1, sY1, sX2, sY2))
    
    # Find out if mouse is pressed down or released
    if self.mouse == 1 and self.grab == 0 and self.mouse_X > -1 and self.mouse_Y > -1:
        self.grabX   = self.mouse_X + self.CATH.new_pos
        self.grabY   = self.mouse_Y
        self.grab    = 1
        self.release = 0
        self.top_label.set_text(str(self.grabX) + ":"+ str(self.grabY))
        
        print('self.grabX', self.grabX)
    
    if self.mouse == 0 and self.release == 0 and self.mouse_X > -1 and self.mouse_Y > -1:
        self.grab     = 0
        self.releaseX = self.mouse_X + self.CATH.new_pos
        self.releaseY = self.mouse_Y
        self.release  = 1
        self.top_label.set_text(str(self.releaseX) + ":"+ str(self.releaseY))
        print('self.releaseX', self.releaseX)
    
    # Body of Selected Lines
    def draw_select_line(mouse_Y, grabY, direction):
        
        if direction == "down":
            self.bY1 = (grabY * self.text_size) + self.EditorY
            self.bY2 = (mouse_Y - grabY) * self.text_size
        
        if direction == "up":
            self.bY1 = (mouse_Y * self.text_size) + self.EditorY
            self.bY2 = ((grabY - mouse_Y) * self.text_size)
        
        self.bX1 = self.EditorX
        self.bX2 = ((self.CATH.max_line_chars) * Width)

    # If mouse click is in the same spot remove any previous selects
    if self.mouse == 0:
        
        if self.get_info == 1:
            self.selected = 1
            
            if self.releaseY < self.grabY:
                startX = self.releaseX - 1
                startY = self.releaseY + 1
                endX   = self.grabX    - 1
                endY   = self.grabY    + 1
            else:
                startX = self.grabX    - 1
                startY = self.grabY    + 1
                endX   = self.releaseX - 1
                endY   = self.releaseY + 1
            
            select(self, (startX, startY),(endX, endY))
            
            if (self.grabX == self.releaseX and self.grabY == self.releaseY):
                clear_selected(self)
                self.selected      = 0
                self.CATH.selected = 0
                self.select_cursor = 0
            
            self.get_info = 0
            
        self.grabbed = 0
        
    # Make sure we are selecting within typable area
    if (self.mouse == 1 and self.mouse_X > -1 and self.mouse_Y > -1
        and self.mouse_Y < self.CATH.total_lines
        and self.mouse_X < self.CATH.max_line_chars and self.scrolling == 0
        and self.selectable == 1):
        
        self.top_label.set_text('SELECTING')
        self.select_cursor = 1
        self.selecting    = 1
        self.get_info     = 1
        self.upwards = 0
        update_text_info(self.CATH)
        # Get length of line text
        try:
            self.self.line_len = len(self.CATH.display_lines[self.mouse_Y])
        except: Exception
        
        if(self.mouseX < self.V_scroll_X and self.mouseY < (self.surface_size[1] - self.scroll_W) and
           self.grabbed == 0):
            clear_selected(self)
            self.grabbed = 1
        
        self.self.line_length = len(self.CATH.lines[self.grabY + self.CATH.real - 1])
        ## Main Cursor Select
        if (self.mouse_X < self.self.line_length + 1
            and self.mouse_X > 0):
            self.top_label.set_text('SEL:' +str(self.self.line_length ))
            # If Cursur is on same line as Selection
            if self.mouse_Y == self.grabY:
                # Selecting right
                if self.grabX <= self.mouse_X:
                    self.cX1 = ((self.grabX) * Width) + self.EditorX
                    self.cX2 = (self.mouse_X - self.grabX) * Width
                    
                # Selecting left
                else:
                    self.cX1 = ((self.mouse_X) * Width)+ self.EditorX
                    self.cX2 = ((self.grabX - self.mouse_X) * Width)
            
            # Else if we are selecting downwards
            elif self.mouse_Y > self.grabY:
                # Selecting right
                self.cX1 = ((self.grabX) * Width) + self.EditorX
                self.cX2 = Width
                
            self.cY1 = (self.grabY * self.text_size) + Y
            self.cY2 = self.text_size
        
        # Selecting down, draw body
        if (self.grabY + 1) < self.mouse_Y and self.selecting == 1:
            draw_select_line(self.mouse_Y, self.grabY + 1, "down")
        
        # Moving up, draw body
        elif self.mouse_Y - 1 < self.grabY and self.selecting == 1:
            draw_select_line(self.mouse_Y + 1, self.grabY, "up") 
        
        # Extend the top most and bottom lines from the start to the end
        # If moving downwards
        if self.grabY < self.mouse_Y:
            # Top line
            # If selecting after text ends on line
            if self.grabX > self.self.line_length:
                self.selX1 = self.EditorX + ((self.self.line_length) * Width)
                self.selX2 = (self.CATH.max_line_chars - self.self.line_length) * Width
            else:
                self.selX1 = self.EditorX + ((self.grabX) * Width)
                self.selX2 = (self.CATH.max_line_chars - self.grabX) * Width
            
            self.selY1 = (self.grabY * self.text_size) + Y
            self.selY2 = self.text_size
            
            # Extend the bottom most line from the start
            self.selX1a = self.EditorX
            self.selY1a = (self.mouse_Y * self.text_size) + Y
            if self.mouse_X > self.self.line_len:
                self.mouse_X = self.self.line_len + 1
                
            self.selX2a = self.mouse_X * Width
            self.selY2a = self.text_size
                
       # If moving upwards
        elif self.grabY > self.mouse_Y:
            
            self.CATH.upwards = 1
            # Bottom line
            if self.grabX > self.self.line_length:
                self.selX2 = self.self.line_length * Width
            else:self.selX2 = (self.grabX) * Width
                
            self.selX1 = self.EditorX
            self.selY1 = (self.grabY * self.text_size) + Y
            self.selY2 = self.text_size                
            
            ### TOP LINE
            if self.self.line_length < self.mouse_X:
                self.selX1a = self.EditorX + (self.self.line_length * Width)
                self.selX2a = (self.CATH.max_line_chars - self.self.line_length) * Width
                
            elif self.mouse_X > 0:    
                self.selX1a = ((self.mouse_X - 1) * Width) + self.EditorX
                self.selX2a = (self.CATH.max_line_chars - self.mouse_X + 1) * Width
            
            self.selY1a = (self.mouse_Y * self.text_size) + Y
            self.selY2a = self.text_size
      
    if (self.mouseX < self.V_scroll_X and self.mouseY > self.EditorY and
        self.grabY == self.mouse_Y and self.mouse == 1 and self.scrolling == 0):
        clear_selected(self, 0)
    
    if self.mouse == 1:
        if ((self.mouse_Y == self.grabY + 1 or self.mouse_Y == self.grabY - 1) and
            self.selecting == 1):
            
            self.bX1    = 0
            self.bY1    = 0
            self.bX2    = 0
            self.bY2    = 0
    """