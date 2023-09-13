#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) and len(tuple_b) >= 2:
        return (tuple_a[0] + tuple_b[0],
                tuple_a[1] + tuple_b[1])

    tuple_aa = tuple_a
    tuple_bb = tuple_b

    if len(tuple_a) >= 1:
        tuple_aa = (tuple_a[0], 0)
    else:
        tuple_aa = (0, 0)

    if len(tuple_b) >= 1:
        tuple_bb = (tuple_b[0], 0)
    else:
        tuple_bb = (0, 0)

    return (tuple_aa[0] + tuple_bb[0],
            tuple_aa[1] + tuple_bb[1])
