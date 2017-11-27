# this file is generated automatically
from syntax_analyzer import LexicalAnalyzer


terminals = ['id', '+', '-', '*', '/', '(', ')']
action_dict = {'0': {'id': 's4', '(': 's5'}, '1': {'+': 's6', '-': 's7', '$': 'acc'}, '2': {'*': 's8', '/': 's9', '+': 'r E->A', '-': 'r E->A', ')': 'r E->A', '$': 'r E->A'}, '3': {'*': 'r A->B', '/': 'r A->B', '+': 'r A->B', '-': 'r A->B', ')': 'r A->B', '$': 'r A->B'}, '4': {'*': 'r B->id', '/': 'r B->id', '+': 'r B->id', '-': 'r B->id', ')': 'r B->id', '$': 'r B->id'}, '5': {'id': 's4', '(': 's5'}, '6': {'id': 's4', '(': 's5'}, '7': {'id': 's4', '(': 's5'}, '8': {'id': 's4', '(': 's5'}, '9': {'id': 's4', '(': 's5'}, '10': {'+': 's6', '-': 's7', ')': 's15'}, '11': {'*': 's8', '/': 's9', '+': 'r E->E + A', '-': 'r E->E + A', ')': 'r E->E + A', '$': 'r E->E + A'}, '12': {'*': 's8', '/': 's9', '+': 'r E->E - A', '-': 'r E->E - A', ')': 'r E->E - A', '$': 'r E->E - A'}, '13': {'*': 'r A->A * B', '/': 'r A->A * B', '+': 'r A->A * B', '-': 'r A->A * B', ')': 'r A->A * B', '$': 'r A->A * B'}, '14': {'*': 'r A->A / B', '/': 'r A->A / B', '+': 'r A->A / B', '-': 'r A->A / B', ')': 'r A->A / B', '$': 'r A->A / B'}, '15': {'*': 'r B->( E )', '/': 'r B->( E )', '+': 'r B->( E )', '-': 'r B->( E )', ')': 'r B->( E )', '$': 'r B->( E )'}}
go_to_dict = {'0': {'E': '1', 'A': '2', 'B': '3', 'id': '4', '(': '5'}, '1': {'+': '6', '-': '7'}, '2': {'*': '8', '/': '9'}, '5': {'E': '10', 'A': '2', 'B': '3', 'id': '4', '(': '5'}, '6': {'A': '11', 'B': '3', 'id': '4', '(': '5'}, '7': {'A': '12', 'B': '3', 'id': '4', '(': '5'}, '8': {'B': '13', 'id': '4', '(': '5'}, '9': {'B': '14', 'id': '4', '(': '5'}, '10': {'+': '6', '-': '7', ')': '15'}, '11': {'*': '8', '/': '9'}, '12': {'*': '8', '/': '9'}}
translate = {'ID': 'id', 'ADD': '+', 'DIV': '/', 'L': '(', 'MUL': '*', 'SUB': '-', 'R': ')'}


# Parser contains method to analyze syntax
class Parser(object):
    tokens = []
    pointer = 0

    @staticmethod
    # this method analyze the syntax of file "input.txt".
    # the syntax is defined in "syntax.y".
    # the lexical is defined in lexical tool PyLex
    # and the lexical analyzer is "LexicalAnalyzer.py" in this project
    # this method will read the input and analyzed the syntax,
    # then output the result(accept, or wrong and where wrong occurred).
    def parse():
        Parser.tokens = LexicalAnalyzer.get_tokens()
        cur_state = '0'
        symbols = []
        cur_stack = ['0']
        next_token = Parser.get_next_token()
        while next_token != "$":
            if "ID" in next_token:
                next_token = "id"
            else:
                next_token = translate[next_token]
            cur_line = action_dict[cur_state]
            if next_token in cur_line.keys():
                next_state = cur_line[next_token]
                if next_state[0] == 's':
                    symbols.append(next_token)
                    cur_state = next_state[1:]
                    cur_stack.append(cur_state)
                else:
                    Parser.push_back()
                    reduce = next_state
                    left_side = reduce[2:].split("->")[0]
                    reduce_list = reduce.split("->")[1].split(" ")
                    for i in range(len(reduce_list)):
                        cur_stack.pop()
                    cur_state = go_to_dict[cur_stack[-1]][left_side]
                    cur_stack.append(cur_state)
                    print(reduce[2:])
            else:
                print("wrong input: " + next_token)
                return
            next_token = Parser.get_next_token()
        print("acc")

    @staticmethod
    # get next token
    # all tokens are from Lexical Analyzer
    def get_next_token():
        if Parser.pointer == len(Parser.tokens):
            return "$"
        else:
            result = Parser.tokens[Parser.pointer]
            Parser.pointer += 1
            return result

    @staticmethod
    # push back current token.
    # (just move the pointer back actually)
    def push_back():
        if Parser.pointer > 0:
            Parser.pointer -= 1
        else:
            print("cannot push back")


Parser.parse()