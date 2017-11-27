

# this class is used to save processed syntax
class SyntaxSaver(object):
    start_symbol = ""
    t_symbol_list = []
    n_symbol_list = []
    syntax_dict = {}

    @staticmethod
    # a big setter
    def register(start, t_list, n_list, syn_dict):
        SyntaxSaver.start_symbol = start
        SyntaxSaver.t_symbol_list = t_list.copy()
        SyntaxSaver.n_symbol_list = n_list.copy()
        SyntaxSaver.syntax_dict = syn_dict.copy()

    @staticmethod
    # getter
    def get_start_symbol():
        return SyntaxSaver.start_symbol

    @staticmethod
    # getter
    def get_terminal():
        return SyntaxSaver.t_symbol_list.copy()

    @staticmethod
    # getter
    def get_non_terminal():
        return SyntaxSaver.n_symbol_list.copy()

    @staticmethod
    # getter
    def get_syntax():
        return SyntaxSaver.syntax_dict.copy()
