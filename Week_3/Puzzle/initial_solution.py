'''puzzle:   https://github.com/bahatyrveronika/bahatyr-veronika-lab8-task2'''
def validate_board(board):
    """
    Checks if the are same number in one column and one row  and in colour blocks
    >>> board = [\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
]
    >>> validate_board(board)
    False
    """
    for row in board:
        row_nums = set()
        for elem in row:
            if elem.isdigit():
                if elem in row_nums:
                    return False
                row_nums.add(elem)
    for col in range(9):
        col_nums = set()
        for row in range(9):
            elem = board[row][col]
            if elem.isdigit():
                if elem in col_nums:
                    return False
                col_nums.add(elem)
    color_nums=set()
    for col in range(9):
        for row in range(8,9):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)
    for col in range(1):
        for row in range(1,8):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)
    color_nums=set()
    for col in range(1,9):
        for row in range(7,8):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)
    for col in range(1,2):
        for row in range(1,7):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)

    color_nums=set()
    for col in range(2,9):
        for row in range(6,7):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)
    for col in range(2,3):
        for row in range(1,6):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)

    color_nums=set()
    for col in range(3,9):
        for row in range(5,6):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)
    for col in range(3,4):
        for row in range(1,5):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)

    color_nums=set()
    for col in range(4,9):
        for row in range(4,5):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)
    for col in range(4,5):
        for row in range(1,4):
            elem=board[row][col]
            if elem.isdigit():
                if elem in color_nums:
                    return False
                color_nums.add(elem)
    return True
