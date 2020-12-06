class SectionNode():
    '''
    SectionNode represents a section of a chapter.

    Variables:
    s_num is the section number
    s_content is the content/text of the section
    s_mode is the section mode
    s_branches are the branches of the section (conditional)

    There are three different modes:
    +++++++++++++++++
    | 0 | Text section.
    | 1 | Text section with prompt.
    | 2 | Text section with branching.
    +++++++++++++++++
    '''
    s_num = 0
    s_content = ''
    s_mode = 0
    s_branches = list()

    def __init__(self, num):
        self.s_num = num

    def add_mode(self, mode):
        self.s_mode = mode

    def add_line(self, line):
        self.s_content = self.s_content + line

    def add_branch(self, num):
        self.s_branches.append(num)

    def get_num(self):
        return self.s_num

    def get_mode(self):
        return self.s_mode

    def get_content(self):
        return self.s_content

    def get_branch(self, location):
        return self.s_branches[location]
        
    def get_num_branches(self):
        return len(self.s_branches)

    def __str__(self):
        return 'Section node #{} with mode {}'.format(self.s_num, self.s_mode)

class ChapterNode():

    c_num = 0
    c_title = ''
    c_sections = dict()

    def __init__(self, c_num):
        self.c_num = c_num

    def add_title(self, title):
        self.c_title = title

    def add_section(self, section):
        self.c_sections[section.get_num()] = section

    def get_num(self):
        return self.c_num

    def get_title(self):
        return self.c_title
    
    def get_section(self, num):
        return self.c_sections[num]

    def get_num_sections(self):
        return len(self.c_sections)

    def __str__(self):
        return 'Chapter node #{}, title \'{}\' with {} sections'.format(
            self.c_num, self.c_title, len(self.c_sections)
        )