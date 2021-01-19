from textgame.reader import Reader
from textgame.item import Item

class Player():

    reader = None
    inventory = list()
    ch_node = None
    ch_num = 0
    s_num_idx = 0
    branch_sec = False

    def __init__(self, path, start_ch, start_inv):
        self.reader = Reader(path)
        self.ch_num = start_ch
        self.inventory = start_inv
        self.ch_node = self.reader.read_chapter(self.ch_num)
        self.s_num = self.ch_node.get_section_nums()[0]

    # Inventory methods

    def item_list(self):
        return self.inventory

    def add_item(self, item):
        if item in self.inventory:
            idx = self.inventory.index(item)
            self.inventory[idx].update(item)
        else:
            self.inventory.append(item)

    # Progression methods

    def progress_next(self, *args):
        if (self.branch_sec):
            self.progress_next_sel(args[0])
        else:
            self.progress_next_def()

    def progress_next_sel(self, select_num):
        pass

    def progress_next_def(self):
        '''
        Moves indexes to the next available section
        '''
        num_sect = self.ch_node.get_num_sections()
        if self.s_num_idx + 1 == num_sect:
            self.ch_num = self.ch_num + 1
            self.s_num_idx = 0
        else:
            self.s_num_idx = self.s_num_idx + 1

    def read(self):
        '''
        Examines the indexes. If the next chapter does not exist,
        it will return a byte object of size two. Else, it will return
        the contents of the section.
        '''
        if self.ch_node.get_num() != self.ch_num:
            if self.ch_num in self.reader.get_chapter_nums():
                self.ch_node = self.reader.read_chapter(self.ch_num)
            else:
                return bytes(2)
        self.s_num = self.ch_node.get_section_nums()[self.s_num_idx]
        return self.ch_node.get_section(self.s_num)