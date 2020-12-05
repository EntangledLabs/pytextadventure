#Imports. Optimize imports for only needed modules
from textgame.reader import Reader

#Global variables.
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

#Color definitions
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

#Initialization. Make sure to optimize inits for specific needed modules.

#Creating the display

#Screens
rd = Reader(chapter=1)
ch = rd.get_chapter_node()
se = ch.get_sections()
print(se)
print(se.get(0).get_content())

quit()