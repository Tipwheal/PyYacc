from SyntaxSaver import SyntaxSaver
import copy


# this class contains methods to calc first set in a syntax
class FirstCalculator(object):
    result = {}

    @staticmethod
    # this method is use to calculate first sets for a syntax
    # and save the result to FirstCalculator.result
    def calc():
        first_dict = {}
        for i in SyntaxSaver.get_non_terminal():
            first_dict[i] = []
        syntax = SyntaxSaver.get_syntax()
        store_dict = {}
        while store_dict != first_dict:
            store_dict = copy.deepcopy(first_dict)
            for i in syntax.keys():
                for j in syntax[i]:
                    for k in j:
                        if k in SyntaxSaver.get_terminal():
                            if k not in first_dict[i]:
                                first_dict[i].append(k)
                            break
                        elif k in SyntaxSaver.get_non_terminal():
                            if "ε" in first_dict[k]:
                                for element in first_dict[k]:
                                    if element != "ε" and element not in first_dict[i]:
                                        first_dict[i].append(element)
                                    if k == j[-1] and "ε" not in first_dict[i]:
                                        first_dict[i].append("ε")
                            else:
                                for element in first_dict[k]:
                                    if element not in first_dict[i]:
                                        first_dict[i].append(element)
                                break
        FirstCalculator.result = first_dict

    @staticmethod
    # input a symbol list to get FIRST(symbol_list)
    # use this after method FirstCalculator.calc() is called and finished
    def first(symbol_list):
        result = []
        for symbol in symbol_list:
            if symbol in SyntaxSaver.get_terminal():
                return symbol
            cur_first = FirstCalculator.result[symbol]
            for i in cur_first:
                if i not in result:
                    result.append(i)
            if "ε" not in cur_first:
                if "ε" in result:
                    result.remove("ε")
                break
        return result


# this class contains methods to calc follow set in a syntax
class FollowCalculator(object):
    result = {}

    @staticmethod
    # calc the FOLLOW set for a syntax and save the result to FollowCalculator.result
    # assume that the syntax has been calculated by other part of the program
    # and the result has been restored in SyntaxSaver
    def calc():
        start = SyntaxSaver.get_start_symbol()
        follow_dict = {}
        for i in SyntaxSaver.get_non_terminal():
            follow_dict[i] = []
        follow_dict[start].append("$")
        syntax = SyntaxSaver.get_syntax()
        for i in syntax.keys():
            for j in syntax[i]:
                for k in range(1, len(j)):
                    if j[k] in SyntaxSaver.get_terminal() and j[k-1] in SyntaxSaver.get_non_terminal():
                        follow_dict[j[k-1]].append(j[k])
        store_dict = {}
        while store_dict != follow_dict:
            for i in syntax.keys():
                store_dict = copy.deepcopy(follow_dict)
                for j in syntax[i]:
                    for k in range(0, len(j)):
                        cur_element = j[k]
                        satisfied = False
                        if k == len(j) - 1 and cur_element in SyntaxSaver.get_non_terminal():
                            satisfied = True
                        elif cur_element in SyntaxSaver.get_non_terminal() and "ε" in FirstCalculator.first(j[k+1:]):
                            satisfied = True
                        if satisfied:
                            for element in follow_dict[i]:
                                if element not in follow_dict[cur_element]:
                                    follow_dict[cur_element].append(element)
        FollowCalculator.result = follow_dict
