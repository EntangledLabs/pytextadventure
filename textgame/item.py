class Item():

    name = ''
    description = ''
    quantity = 0
    modifiers = dict()

    def __init__(self):
        pass

    def update(self, item):
        attr = item.get_attr()
        if self.name == attr[0]:
            self.quantity = self.quantity + attr[2]
            for key in self.modifiers.keys():
                if key in attr[3].keys():
                    pass

    def get_attr(self):
        return (self.name, self.description, self.quantity, self.modifiers)