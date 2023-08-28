#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(list_length):
        try:
            dev = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            dev = 0
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
            dev = 0
        except IndexError:
            print("out of range")
            dev = 0
        finally:
            my_list.append(dev)
    return my_list
