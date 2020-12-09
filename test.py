#Imports. Optimize imports for only needed modules
from textgame.reader import Reader
from textgame.node import SectionNode

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
cn = Reader().read_chapter(1)
#print(str(cn))

for i in range(0, cn.get_num_sections()):
    sn = cn.get_section(i)
    print('Section {} with contents \"{}\"'.format(sn.get_num(), sn.get_content()))

quit()