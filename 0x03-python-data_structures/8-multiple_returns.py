#!/usr/bin/python3

def multiple_returns(sentence):
    len_char = ()
    if (len(sentence) == 0):
        len_char = len(sentence), None
    else:
        len_char = len(sentence), sentence[0]
    return (len_char)
