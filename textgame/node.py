class Node():

    id = 0
    contents = ''

    def __init__(self, id):
        self.id = id

    def add_contents(self, contents):
        self.contents = contents

    def my_id(self):
        return self.id

class ChapterNode(Node):

    sections = {}
    title = ''

    def __init__(self, chnum):
        super().__init__(chnum)

    def add_title(self, title):
        self.title = title

    def add_section(self, section):
        self.sections[section.my_id()] = section

    def get_section(self, id):
        return self.sections[id]

    def get_title(self):
        return self.title
class SectionNode(Node):

    branching = False
    branch_ids = []
    prompt = False

    def __init_(self, sectnum):
        super().__init__(sectnum)

    def add_branch(self, id):
        self.branching = True
        self.branch_ids.append(id)

    def req_prompt(self):
        self.prompt = True