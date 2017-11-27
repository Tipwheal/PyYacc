import SyntaxReader
from SyntaxSaver import SyntaxSaver


# this class is used to process the syntax defined in "syntax.y"
# and saved the processed syntax to SyntaxSaver
class SyntaxProcessor(object):
    STATE_START = 0
    STATE_DEF = 1
    STATE_SYN = 2
    predefine_dict = {
        "SYN_R": ")", "SYN_L": "(", "SYN_OR": "|", "SYN_ADD": "+", "SYN_SUB": "-", "SYN_MUL": "*",
        "SYN_DIV": "/"
    }

    @staticmethod
    # read the comment of this class please...
    def process_syntax():
        tokens = SyntaxReader.get_tokens()
        cur_state = SyntaxProcessor.STATE_START
        t_symbol_list = []
        n_symbol_list = []
        syntax_dict = {}
        start_symbol = ""
        cur_n = ""
        sub_list = []
        after_to = False
        for token in tokens:
            if token == "TK_START":
                cur_state = SyntaxProcessor.STATE_DEF
            elif token == "SN_START":
                cur_state = SyntaxProcessor.STATE_SYN
            elif cur_state == SyntaxProcessor.STATE_DEF and token != "DOT":
                t_symbol_list.append(token[3:])
            elif cur_state == SyntaxProcessor.STATE_SYN:
                if not after_to and "ID" in token:
                    cur_n = token[3:]
                    if len(n_symbol_list) == 0:
                        start_symbol = cur_n
                    if cur_n not in n_symbol_list and cur_n not in t_symbol_list:
                        n_symbol_list.append(cur_n)
                elif token == "TO":
                    after_to = True
                elif token == "END":
                    if cur_n not in syntax_dict.keys():
                        syntax_dict[cur_n] = []
                    syntax_dict[cur_n].append(sub_list)
                    sub_list = []
                    cur_n = ""
                    after_to = False
                elif token == "SYN_OR":
                    if cur_n not in syntax_dict.keys():
                        syntax_dict[cur_n] = []
                    syntax_dict[cur_n].append(sub_list)
                    sub_list = []
                else:
                    if "ID" in token:
                        n_syn = token[3:]
                        if n_syn not in n_symbol_list and n_syn not in t_symbol_list:
                            n_symbol_list.append(n_syn)
                        sub_list.append(n_syn)
                    elif token in SyntaxProcessor.predefine_dict.keys():
                        real_token = SyntaxProcessor.predefine_dict[token]
                        if real_token not in t_symbol_list:
                            t_symbol_list.append(real_token)
                        sub_list.append(real_token)
        SyntaxSaver.register(start_symbol, t_symbol_list, n_symbol_list, syntax_dict)

