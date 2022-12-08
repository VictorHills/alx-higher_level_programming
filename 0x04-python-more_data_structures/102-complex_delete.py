#!/usr/bin/python3
def complex_delete(a_dic, val):
    list_keys = list(a_dic.keys())

    for val_dic in list_keys:
        if val == a_dic.get(val_dic):
            del a_dic[val_dic]

    return (a_dic)
