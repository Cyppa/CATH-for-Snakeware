# CATH-for-Snakeware
Cath Editor Designed for integration with Snakeware Window Manager

Released under the GPL 3+

This version of CATH editor is designed to soley work in Snakeware python based OS.

CATH is built in Python with Pygame and Pygame_gui 0.5.6 or newer as its front end.

The backend is not necessarily reliant on Pygame_gui however.

The program is still in early development and WILL break. It does allow for basic text editing,
saving and opening text files. Do save very regulalry if deciding to use it.

To RUN:

Copy the contents into directory:

'....snakewm/apps/tools/'

and run snakewm.py.

You will then find the entry 'CATH' under the tools drop-down menu.

*** IMPORTANT NOTES
Currently moving the window results in mouse faults as relative mouse coordinates don't have a way to be updated yet.
However window resizing does work if resized from the bottom or right boundaries.

Also text selecting isn't functional as the code needs updating so there are no copy/ paste functions.

A few of the buttons in the options menu aren't functional either. However text re-sizing works and theme chaning mainly 
works too.

The search, replace functions work for the most part. The 'Goto' button will work and vertical scrolling works too.

Things like Horizontal Scrolling will be integreted soon and most other functions too.

Happy Editing...

