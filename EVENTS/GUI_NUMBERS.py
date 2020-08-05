import pygame

from ..Editor.SHARED import Col

# Method to count amount of digits in a number
def count(integer):
    count = 0
    while (integer > 0):
        integer = integer//10
        count   = count + 1
    return count

def numbers(self, surface):
    
    if self.numbers == 1:
        
        # Find out how many digits we need to display
        # By getting the amount of lines in the text file
        if   len(self.CATH.lines) < 10000: self.nums = 4
        elif len(self.CATH.lines) < 1000 : self.nums = 3
        elif len(self.CATH.lines) < 100  : self.nums = 2
        self.EditorX = self.EditorX_old + (self.nums * self.CATH.text_width)
        
        nlX1 = self.CATH.text_width * self.nums
        nlY1 = self.EditorY
        nlX2 = nlX1
        nlY2 = self.surface_size[1] - self.offset - self.scroll_W
        
        # Draw line
        number_line = pygame.draw.line(surface, Col("grey", 60),
                                      (nlX1, nlY1), (nlX2, nlY2), 1)
        
        font = pygame.font.Font(self.CATH.FONT, self.CATH.text_size)
        
        col = 0
        for l in range(self.CATH.total_lines):
            self.display_number = l + self.CATH.real + 1
            
            # Put '0's in front of smaller numbers
            count_ = self.nums - count(l + self.CATH.real + 1)
            if count_ == 1: text =         str(self.display_number)
            if count_ == 2: text = "0"   + str(self.display_number)
            if count_ == 3: text = "00"  + str(self.display_number)
            if count_ == 4: text = "000" + str(self.display_number)
            
            nX = self.EditorX_old
            nY = self.EditorY + (self.CATH.text_size * l)
            
            # Change colour of every 2nd number
            col = (col + 1) % 2
            if col == 1: colour = "grey"
            else:        colour = "white"
            
            # Render result
            Text = font.render(text, True, Col(colour, 65))
            surface.blit(Text, (nX, nY))
    
    else: self.nums = 0
        
        
        
        
