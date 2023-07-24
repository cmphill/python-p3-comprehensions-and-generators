#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = []
    [even_nums.append(i) for i in num_list if i % 2 == 0]
    return even_nums

def make_exclamation(sentence_list):
    exclamation_list = [i + "!" for i in sentence_list]
    return exclamation_list