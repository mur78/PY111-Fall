def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    # (()) - с помощью стэка проверить корректность скобок
    #

    brackets_list = []
    cnt_list_valid = 0
    cnt_list_not_valid = 0

    if brackets_row == "":
        return True
    for val in brackets_row:
        if val == "(":
            cnt_list_valid += 1
            brackets_list.append(val)
        elif val == ")":
            cnt_list_not_valid += 1
            if brackets_list:
                brackets_list.pop()
            else:
                return False
    else:
        if cnt_list_valid != cnt_list_not_valid:
            return False
        else:
            return True

if __name__ == '__main__':
    print(check_brackets("((((())))"))
    print(check_brackets("()()()()()"))
