from field import Field


def get_binary_list_by_obj_path(field: Field, path):
    """

    :param field:
    :param path:
    :return:
    [[True, False, False],
     [False, True, False],
     [True, True, True]] или что-то вроде того
    """
    binary_list = []
    for row in field.cells:
        binary_row = []
        for cell in row:
            binary_row.append(cell.path == path)
        binary_list.append(binary_row)
    return binary_list

def is_win(bl) -> bool:
    """

    :param bl: binary list
    :return:
    """
    if bl[0][0] == bl[1][1] == bl[2][2] == True:
        return True
    if bl[0][2] == bl[1][1] == bl[2][0] == True:
        return True
    if bl[0][0] == bl[1][0] == bl[2][2] == True:
        return True
    if bl[0][1] == bl[1][1] == bl[2][1] == True:
        return True
    if bl[0][2] == bl[1][2] == bl[2][2] == True:
        return True
    if bl[0][0] == bl[0][1] == bl[0][2] == True:
        return True
    if bl[1][0] == bl[1][1] == bl[1][2] == True:
        return True
    if bl[2][0] == bl[2][1] == bl[2][2] == True:
        return True
    return False

def who_won(field: Field):
    """

    :param field: класс Field из field.py
    :return: None, "first" или "second"
    """
    xs = get_binary_list_by_obj_path(field, "imgs/x.png")
    os = get_binary_list_by_obj_path(field, "imgs/o.png")
    if is_win(xs):
        return "first"
    if is_win(os):
        return "second"
    return None
