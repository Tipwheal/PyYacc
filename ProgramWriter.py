from ParsingTable import ParsingTable
from SyntaxSaver import SyntaxSaver


# writer will get the parsing table from previous part of the program,
# and attach some important data structures to "ParserTemplate.py"
# to generate the final SyntaxAnalyzer.
class Writer(object):

    @staticmethod
    # this method read the text in "ParserTemplate.py"
    # and rewrite them to "SyntaxAnalyzer.py".
    # add terminal sets, ACTION and GO TO table to "SyntaxAnalyzer"
    def write():
        f = open("template/ParserTemplate.py", "r")
        lines = f.readlines()
        f.close()
        f = open("syntax_analyzer/SyntaxAnalyzer.py", "w")
        f.write("# this file is generated automatically\n")
        for i in range(1, len(lines)):
            f.write(lines[i])
            if i == 2:
                f.write("\n")
                f.write("terminals = ")
                f.write(str(SyntaxSaver.get_terminal()))
                f.write(str())
                f.write("\n")
                f.write("action_dict = ")
                f.write(str(ParsingTable.action_dict))
                f.write("\n")
                f.write("go_to_dict = ")
                f.write(str(ParsingTable.go_to_dict))
                f.write("\n")