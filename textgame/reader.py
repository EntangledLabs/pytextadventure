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

from textgame.node import *
import configparser

class Reader():

    '''
    Performs init of the Reader.
    
    Supported kwargs are:
    chapter <- read a chapter file
    credits <- read a credits file
    instructions <- read an instructions file
    '''
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'credits':
                pass
            if key == 'chapter':
                self.chapter = value
                self.read_chapter()
            if key == 'instructions':
                pass

    def read_chapter(self):
        # File read
        filename = 'chapter{}.txt'.format(self.chapter)
        cfile = open(filename, 'rt')
        
        # ChapterNode creation
        chnode = ChapterNode(self.chapter)

        # Read lines and determine what to do with them
        lines = cfile.readlines()
        for i in range(0,len(lines)):
            line = lines[i]
            if i == 0:
                chnode.add_title(line)
            else:
                if (line[0].isdigit() and line[len(line)-1] == '='):
                    sectnode = self.interpret_sequence(line)
                else:
                    pass

    def interpret_sequence(self, sequence):
        return Node(0)