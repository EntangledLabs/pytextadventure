from textgame.reader import Reader
from textgame.items import *

class Player():

    reader = Reader()
    inventory = dict()
    ch_node = None
    ch_num = 0
    s_num_idx = 0

    def __init__(self, start_ch, start_inv):
        self.reader.read_chapter(start_ch)
        self.inventory = start_inv
        self.ch_node = self.reader.read_chapter(self.ch_num)
        self.s_num = self.ch_node.get_section_nums()[0]

    # Progression methods

    def progress_next(self):
        '''
        Overarching progression. Runs both progress_next_chapter() and progress_next_section()
        '''
        pass

    def progress_next_chapter(self):
        self.ch_num = self.ch_num +1

    def progress_next_section(self):
        self.s_num_idx = self.s_num_idx + 1

    # Read and return methods

    def read(self):
        pass