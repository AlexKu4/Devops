def concatenate_str(s1, s2):
    return s1 + " " + s2 + ""


def sum_numbers(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    return -1


def devide_nums(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int) and num2 != 0:
        return num1 // num2
    else:
        return -1
