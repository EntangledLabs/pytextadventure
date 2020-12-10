class Item():

    name = ''
    description = ''
    quantity = 0
    modifiers = dict()

    def __init__(self):
        pass

    def update(self, item):
        pass

    def get_attr(self):
        return (self.name, self.description, self.quantity, self.modifiers)