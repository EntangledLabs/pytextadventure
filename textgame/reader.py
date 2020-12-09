from textgame.node import *
import configparser, re

class Reader():
    '''
    The Reader class takes text files relevant to TextGame and interprets them
    into the proper node structure.

    Reader will specifically cover chapter files and a credits file. To add
    additional reading capabilities, it should be as simple a matter as
    extending Reader and adding the functionality from there.

    Upon init, Reader will search for the specified chapter number or, if otherwise
    specified, special files. It will parse the file and attempt to create a
    node structure from the contents.

    Chapter files are specifically named "chapter[chapter number].txt"

    The first line in the chapter file is the chapter title.

    Sections in chapter files are similar in syntax to those in HTML.
    There is a character sequence that acts as a code of interpretation.
    It will appear like this:

        1==

    or:

        14p===

    or:

        32e=

    The shortest possible sequence is three characters, but it can technically
    be infinite in length.

    The first characters are the section number. This numbering is unique to each
    file, so it is unnecessary to continue numbering betwen files. Section numbering
    should begin at 1, the starting section for the chapter. Numbers with multiple
    digits are treated as such. For example:

        1==

    indicates section one, while:

        14325==

    indicates section 14325, and so on.

    The next character indicates if there are any special modes. The following table
    provides a list of supported special modes:

    ++++++++++++
    | = | No special mode. This is a purely textual section for storytelling.
    | p | User prompt. The user needs to type a response to the text.
    | b | Branching. The user needs to select an option for the next node.
    | e | End of section. Indicates the end of a section.
    ++++++++++++

    The next characters exist only if the special mode is Branching.

    Each 'choice' requires both the character 'c' proceeded by the number of the section
    the choice leads to.

    The final character in a sequence is always an equal sign.

    Here is an example of a branching section:

        3bc13c14c15= <- Section 3, Branching. Three possible choices: sections 13, 14, and 15.
        Story goes here.
        3e= <- Section 3, end.

    and a textual section:

        4== <- Section 4, no special mode.
        Story goes here.
        4e= <- Section 4, end.
    '''
    # Class variables

    def read_chapter(self, ch_num):
        
        # File read
        filename = './stories/chapter{}.txt'.format(ch_num)
        cfile = open(filename, 'rt')

        # Chapter creation
        c_node = ChapterNode(ch_num)
        title = cfile.readline()
        c_node.add_title(title.strip('\n'))

        # Find out how many sections there are
        lines = cfile.readlines()
        section_nums = list()
        for i in range(0,len(lines)):
            lines[i] = lines[i].strip('\n')
            if re.match('[0-9]+[=bp]([c][0-9]+)*[=]', lines[i]):
                section_nums.append(int(re.match('[0-9]+', lines[i]).group(0)))
        
        # Create relevant number of SectionNode
        nodes = dict()
        for i in section_nums:
            nodes[section_nums[i]] = SectionNode(section_nums[i])

        # Take the text from 'lines'
        index = 0
        for line in lines:
            # If a non-exit sequence is detected, change SectionNode properties.
            if re.match('[0-9]+[=bp]([c][0-9]+)*[=]', line):
                index = int(re.match('[0-9]+', line).group(0))
                nodes[index].add_mode(self.read_mode(line))
                if (self.read_mode(line) == 2):
                    br = self.read_branches(line)
                    for i in br:
                        nodes[index].add_branch(i)

            # If an exit sequence is detected, add SectionNode to the ChapterNode
            elif re.match('[0-9]+[e][=]', line):
                c_node.add_section(nodes[index])

            # If no sequence detected, add the line to the SectionNode
            else:
                nodes[index].add_line(line)

        return c_node
    
    def read_mode(self, sequence):
        '''
        Looks for the mode in the sequence
        '''
        mode = re.search('[=bp]', sequence).group(0)
        if mode == '=':
            return 0
        elif mode == 'p':
            return 1
        else:
            return 2


    def read_branches(self, sequence):
        '''
        Looks for the branches in the sequence
        '''
        br = re.findall('[c][0-9]+', sequence)
        for i in br:
            i = int(i[1:])
        return br

    def read_credits(self):
        pass