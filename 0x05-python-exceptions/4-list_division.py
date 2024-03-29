#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            val = 0
            print("division by 0")
        except (TypeError):
            val = 0
            print("wrong type")
        except (IndexError):
            val = 0
            print("out of range")
        finally:
            result_list.append(val)
    return result_list
