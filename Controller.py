from SyntaxProcessor import SyntaxProcessor
from Modifier import Modifier
from ParsingTable import ParsingTable
from FunctionCalculator import *
from ProgramWriter import Writer

# this file is the entry of the program
# run this script to get the syntax analyzer name "SyntaxAnalyzer.py"

SyntaxProcessor.process_syntax()
Modifier.add_dot()
FirstCalculator.calc()
FollowCalculator.calc()
ParsingTable.calc_item_set()
Writer.write()

