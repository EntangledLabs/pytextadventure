class ChapterNode():

    id = 0
    section = {}
    title = ''

    def __init__(self, id):
        self.id = id

    def add_title(self, title):
        self.title = title

    def add_section(self, section, id):
        self.section[id] = section

    def get_section(self, id):
        return self.section[id]
    
    def get_sections(self):
        return self.section

    def get_title(self):
        return self.title

    def get_id(self):
        return self.id

    def to_string(self):
        return 'Chapter node {} with title \"{}\" and sections {}.'.format(self.id, str(self.title), str(self.section))

class SectionNode():

    id = 0
    contents = []
    branching = False
    branch_ids = []
    prompt = False

    def __init__(self, id):
        self.id = id

    def req_prompt(self):
        self.prompt = True

    def add_content(self, contents):
        self.contents.append(contents)

    def add_branches(self, ids):
        self.branching = True
        self.branch_ids.append(ids)

    def get_content(self):
        return self.contents

    def get_branches(self):
        return self.branch_ids

    def get_branch(self, id):
        return self.branch_ids[id]

    def get_id(self):
        return self.id

    def to_string(self):
        return 'Section node {} with contents {}.'.format(self.id, str(self.contents))