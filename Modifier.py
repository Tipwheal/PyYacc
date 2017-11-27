from SyntaxSaver import SyntaxSaver


# this class is use to modify the context free grammar
# in order to fit the requirements of LR grammar
class Modifier(object):

    @staticmethod
    # add ' to the start symbol of the syntax
    # assume that the syntax has been calculated and saved in SyntaxSaver
    def add_dot():
        start = SyntaxSaver.start_symbol
        new_start = start + "'"
        SyntaxSaver.syntax_dict[new_start] = [[start]]
        SyntaxSaver.start_symbol = new_start
        SyntaxSaver.n_symbol_list.append(new_start)