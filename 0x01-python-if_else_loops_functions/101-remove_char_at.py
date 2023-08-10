#!usr/bin/python3

def remove_char_at(str, n):
    copy_str_n = ""

    i = 0
    for i in range(0, len(str)):
        if i == n:
            continue
        else:
            copy_str_n += str[i]

    return copy_str_n
