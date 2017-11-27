from SyntaxSaver import SyntaxSaver
from FunctionCalculator import FollowCalculator


# this class contains some method to calc all item sets
# and provide an interface to get all the item sets outside.
class ParsingTable(object):
    item_sets = {}
    go_to_dict = {}
    action_dict = []

    @staticmethod
    # this method is used to calc all item set for the syntax calculated by previous part of program
    def calc_item_set():
        start = SyntaxSaver.get_start_symbol()
        syntax = SyntaxSaver.get_syntax()
        n_list = SyntaxSaver.get_non_terminal()
        t_list = SyntaxSaver.get_terminal()
        result = {}
        item = (start, syntax[start][0].copy())
        item[1].insert(0, "·")
        i_0 = ParsingTable.calc_i_0(item, n_list, syntax)
        i_count = 0
        result[str(i_count)] = i_0
        i_count += 1
        go_to_dict = {}
        cur_count = 0
        while cur_count < i_count:
            for terminal in n_list + t_list:
                next_items = ParsingTable.next_main_item_set(result[str(cur_count)], terminal)
                if len(next_items) != 0:
                    i_n = ParsingTable.calc_i_n(next_items, n_list, syntax)
                    add_new_state = ParsingTable.add_i_n(i_n, result, go_to_dict, terminal, i_count, str(cur_count))
                    if add_new_state:
                        i_count += 1
            cur_count += 1
        ParsingTable.item_sets = result
        ParsingTable.go_to_dict = go_to_dict
        ParsingTable.action_dict = ParsingTable.calc_action_dict()

    @staticmethod
    def calc_action_dict():
        action_dict = {}
        for i in range(len(ParsingTable.item_sets)):
            action_dict[str(i)] = {}
        for key in ParsingTable.go_to_dict.keys():
            for inner_key in ParsingTable.go_to_dict[key]:
                if inner_key in SyntaxSaver.get_terminal():
                    action_dict[key][inner_key] = "s" + (ParsingTable.go_to_dict[key][inner_key])
        for key in ParsingTable.item_sets.keys():
            item_set = ParsingTable.item_sets[key]
            for production in item_set:
                left = production[0]
                right = production[1]
                if left == SyntaxSaver.get_start_symbol() and right[-1] == "·":
                    action_dict[key]["$"] = "acc"
                elif right[-1] == "·":
                    for term in FollowCalculator.result[left]:
                        # override shift by reduce when shift/reduce conflict occur.
                        action_dict[key][term] = "r " + left + "->" + " ".join(right[:-1])
        return action_dict

    @staticmethod
    # return if there is new item sets added
    def add_i_n(item_set, all_item_sets, go_to_dict, path, i_count, cur_count):
        exists = False
        place = ""
        for key in all_item_sets:
            temp_item_set = all_item_sets[key]
            if temp_item_set == item_set:
                exists = True
                place = key
                break
        if cur_count not in go_to_dict.keys():
            go_to_dict[cur_count] = {}
        if exists:
            go_to_dict[cur_count][path] = place
            return False
        else:
            all_item_sets[str(i_count)] = item_set
            go_to_dict[cur_count][path] = str(i_count)
            return True

    @staticmethod
    # this method is used to calc main part of next item set
    # if there is no item in the item set, return []
    # add · in this method
    def next_main_item_set(prev_items, path):
        result = []
        for item in prev_items:
            right_part = item[1]
            index = right_part.index("·") + 1
            if index < len(right_part) and right_part[index] == path:
                temp_list = right_part.copy()
                temp_list.remove("·")
                temp_list.insert(index, "·")
                result.append((item[0], temp_list))
        return result

    @staticmethod
    def calc_i_n(items, n_list, syntax):
        cur_set = items.copy()
        size = len(cur_set)
        while True:
            tmp_set = []
            for item in cur_set:
                right = item[1]
                index = right.index('·') + 1
                if index >= len(right):
                    continue
                elif right[index] in n_list:
                    for temp_item in syntax[right[index]]:
                        dot_item = temp_item.copy()
                        dot_item.insert(0, '·')
                        tmp_set.append((right[index], dot_item))
            for item in tmp_set:
                if item not in cur_set:
                    cur_set.append(item)
            if len(cur_set) == size:
                break
            else:
                size = len(cur_set)
        return cur_set

    @staticmethod
    # this method is used to calc the first item set I0
    def calc_i_0(item, n_list, syntax):
        cur_set = [item]
        size = len(cur_set)
        while True:
            tmp_set = []
            for item in cur_set:
                right = item[1]
                index = right.index('·') + 1
                if index >= len(right):
                    continue
                elif right[index] in n_list:
                    for temp_item in syntax[right[index]]:
                        dot_item = temp_item.copy()
                        dot_item.insert(0, '·')
                        tmp_set.append((right[index], dot_item))
            for item in tmp_set:
                if item not in cur_set:
                    cur_set.append(item)
            if len(cur_set) == size:
                break
            else:
                size = len(cur_set)
        return cur_set
