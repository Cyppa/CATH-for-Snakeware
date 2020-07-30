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

## SQUARE
import pygame as P

# Colour Selector
# Lets us choose a colour and it's intensity
# '0' is darkest to '100' which is brightest
def Col(col, num = 100):
        
    X = int((255 / 100) * num)
    colour = (0,    0,    0)
    
    if   col ==   "black": colour = (0,    0,    0)
    elif col ==    "grey": colour = (X,    X,    X)
    elif col ==     "red": colour = (X,    0,    0)
    elif col ==   "green": colour = (0,    X,    0)
    elif col ==    "blue": colour = (0,    0,    X)
    elif col ==  "yellow": colour = (X,    X,    0)
    elif col ==    "cyan": colour = (0,    X,    X)
    elif col == "magenta": colour = (X,    0,    X)
    elif col ==   "white": colour = (255, 255, 255)
    
    return(colour)

class Square:
    
    def __init__(self, screen, X, Y, width, length, orient = "vertical",
                 colour = "grey", fill = True, line_width = 0):
        
        self.screen, self.fill   = screen, fill
        self.X, self.Y           = X, Y
        self.width, self.length  = width, length
        self.orient, self.colour = orient, colour
        self.line_width          = line_width
        
        if self.line_width == 0:
            self.line_width      = round(width / 20)
        
        if orient == "horizontal":
            self.dim1, self.dim2 = length, width

        if orient == "vertical":
            self.dim1, self.dim2 = width, length
            
        self.x1, self.y1 = X, Y
        self.x2, self.y2 = self.x1 + self.dim1, self.y1 + self.dim2

        self.p1, self.p2  = (self.x1, self.y1), (self.x2, self.y1) 
        self.p3, self.p4  = (self.x2, self.y2), (self.x1, self.y2)
        self.D            = [self.p1, self.p2, self.p3, self.p4]
        
        if self.orient == "horizontal":
                self.width, self.length = self.length, self.width
                
    def draw(self, screen):
        
        if self.fill == True:
            
            if self.colour == "grey": CX = 50
            else: CX = 100
            P.draw.rect(screen, Col(self.colour, CX),
                        (self.X, self.Y, self.width, self.length))
        
        for l in range(len(self.D)):
            if l < 2: C = 30
            else: C = 70
            P.draw.line(screen, Col(self.colour, C), self.D[l], self.D[(l+1)%4],
                        self.line_width)
            