#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_new_a = tuple_a + (0, 0)
    tuple_new_b = tuple_b + (0, 0)

    return (tuple_new_a[0] + tuple_new_b[0],
            tuple_new_a[1] + tuple_new_b[1])
