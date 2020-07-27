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

### Create variable used by GUI
def create_gui_variables(self, position):
    size = (768, 600)
    
    self.window_bar       = [0, 0, 756, 42]
    self.window_offset    = [position[0], position[1]]
    self.window_position  = [position[0], position[1]]

    self.surface_size     = self.get_container().get_size()
    self.size             = self.surface_size
    self.mouse            = 0
    self.is_active        = True
    self.rel_X            = 0
    self.rel_Y            = 0
    
    self.W                     = 768                    # Window WIDTH
    self.H                     = 600                    # Window HEIGHT
    
    self.buttonY               = 30                     # Height of buttons
    self.buttonX               = 100                    # Width of buttons
    self.panel_W               = size[0]                # Width of panels
    self.search_button_pressed = False
    self.text_entryX           = round((self.panel_W - (self.buttonX * 2.5))/ 2) - 4 # Width in pixels of 'search' text_entry boxes
    self.offset                = 2                      # General panel/ area offset
    
    self.FONT                  = self.app_path + "/ASSETS/ubuntu-mono/UbuntuMono-R.ttf"
    self.text_size             = 18
    self.text_width            = round(self.text_size / 2)
    self.EditorX               = self.offset                         # Starting X position of text editor backend
    self.EditorY               = (self.buttonY * 2) + self.text_size # Starting Y position of text editor backend also Height of Both Panels
    self.Ewidth                = size[0]                             # Total width of text editor backend
    self.Eheight               = size[1] - self.EditorY              # Total height of text editor backend
    self.FPS                   = 60
    
    self.Panel_size            = self.buttonY + (self.offset *2) # Height of PANELS
    self.mouse_updater         = 1         # Do we need mouse updating?
    self.scroll_W              = 16        # Vertical scroll bar width in pixels
    self.body_Y                = self.H - (self.Panel_size * 2) - self.offset # Total height of text editor backend/ writeable area
    self.mouse                 = 0         # 1 = mouse click down, 0 = mouse released
    self.character_X           = 1         # text character number
    self.line_Y                = 1         # text line number
    self.rock_bottom           = 0         # 1 = last line of text being displayed, 0 = otherwise
    self.bar_width             = 27        # Title Bar height in pixels
    self.mouseX                = 0         # Relative X mouse coord to Window left
    self.mouseY                = 0         # Relative Y mouse coord to Window top
    self.V_scroll_X            = self.panel_W - self.scroll_W
    self.V_scroll_Y            = self.EditorY
    self.scroll_TOP            = self.V_scroll_Y 
    self.scrolled              = 0
    self.scrolling             = 0
    self.V_scr_grabbed         = 0
    self.V_scr_grab            = [0,0]
    self.V_step                = self.EditorY
    self.V_unit                = 0
    self.V_line_unit           = 0
    self.V_move                = 0
    self.V_bar_length          = 0
    self.move_lines            = 0
    self.window_active         = False
    self.V_release             = 0
    self.temp_var              = 0
    self.V_move                = 0
    self.V_col                 = 100
    self.window_move           = False
    self.over_lines            = 0
    self.line_unit             = 0
    self.prev_sizeX            = 0
    self.prev_sizeY            = 0
    self.window_move           = False
    self.win_grab              = [0,0]
    self.GRAB                  = [0,0]
    self.grab_line             = 0
    
    # Horozontal Scrolling
    self.longest_line          = 0
    self.over_chars            = 0
    self.H_bar_length          = 0
    self.H_char_unit           = 0
    self.H_unit                = 0
    self.char_unit             = 0
    self.temp_varH             = 0
    self.H_scr_grab            = 0
    self.H_scr_grabbed         = 0
    self.H_release             = 0
    self.H_col                 = 100
    self.grab_char             = 0
    self.H_move                = 0
    self.H_scroll_E            = 0
    
    self.file_save             = 0
    self.file_open             = 0
    self.editor_text           = 1         # 1 = we can type, 0 = no able to type
    self.selectable            = 0
    self.grid_was_on           = 0         # grid related
    self.grid_on               = 0         # 1 = yes, 0 = no
    self.grid_strength         = 0
    self.cursor_on             = 0
    self.themes                = ["default", "light", "dark"]
    self.default_theme         = 'ASSETS/themes/theme.json'
    self.theme_counter         = 0
    self.file_string           = ""
    self.selected              = 0         # 1 = a selection has just been made
    self.selecting             = 0
    self.save_error            = False
    
    # Search Replace
    self.previous_string       = ""        # help figure out if search string has changed
    self.not_found             = 0         # 1 = yes, 0 = no. Search file not found
    self.occurance             = 0         # how many instances of search string found
    self.Occounter             = []        # List which stores with line and position instances (of found search string) reside
    self.re_search             = 0         # 1 = re-run search analysis operation
    
    self.numbers               = 0 # Do we need character offset for line numbers
    self.only_display          = 0
    self.bottom                = 0 # Helps figure out if last line is on screen
    self.display_bottom        = 0 # Ditto
    
    self.label_W               = self.panel_W - (self.offset * 2) - (self.buttonX * 2)
    self.stat_label_chars      = self.label_W // self.text_width
    
    # Create minimum window dimensions
    min_X           = (5.5 * self.buttonX) - (self.offset *4)
    min_Y           = self.Panel_size + self.bar_width + (self.text_size * 8)
    self.set_minimum_dimensions((min_X, min_Y))
    
    print('Variables Loaded')