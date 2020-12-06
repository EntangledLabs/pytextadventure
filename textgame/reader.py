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

    14325====

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

import configparser, re

class Reader():

    # Class variables
    chapter_num = 0
    chapter_title = ''
    chapter_sections = {}

    def read_chapter(self, ch_num):
        
        # File read
        filename = './stories/chapter{}.txt'.format(ch_num)
        cfile = open(filename, 'rt')
        
        # Chapter creation
        self.chapter_num = ch_num
        self.chapter_title = cfile.readline().strip('\n')

        # Read lines and determine what to do with them
        lines = cfile.readlines()
        for line in lines:
            t = line.strip('\n')
            if (re.match('[0-9]+[=ebp].*[=]', t)):
                interpret = self.interpret_sequence(t)
                if interpret == 'e':

            else:
                


    '''
    Takes a sequence and interprets it to the proper section node configuration
    '''
    def interpret_sequence(self, sequence):
        # Read sequence and split into its sections
        part1 = re.match('[0-9]+', sequence).group(0)
        part2 = re.search('[=ebp]', sequence).group(0)
        part3 = re.findall('[c][0-9]+', sequence)

        for i in part3:
            i = i[1:]
            i = int(i)

        #print('Section {}, mode {}'.format(part1,part2))

        if (part2 == '='):
            return SectionNode(int(part1))
        elif (part2 == 'b'):
            nd = SectionNode(int(part1))
            nd.add_branches(part3)
            return nd
        elif (part2 == 'p'):
            nd = SectionNode(int(part1))
            nd.req_prompt()
            return nd
        elif (part2 == 'e'):
            return 'e'