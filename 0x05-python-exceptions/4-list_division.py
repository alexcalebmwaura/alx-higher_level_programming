#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists.

    Args:
        my_list_1 (list): Integer 1
        my_list_2 (list): Interger 2
        list_length (int): elements to divided.

    Returns:
        Returns a new list (length = list_length) with all divisions
    """
    new_list = []
    for a in range(0, list_length):
        try:
            div = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
