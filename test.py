#Imports. Optimize imports for only needed modules
from textgame.player import Player

player = Player('./data/', 1, dict())

for i in range(0, 7):
    sect = player.read()
    if isinstance(sect, bytes):
        print(sect)
    else:
        print(sect.get_content())
        player.progress_next()

quit()