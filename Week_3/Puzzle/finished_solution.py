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
    if not (isinstance(board, list) and len(board) == 9):
        return False
    for line in board:
        if not (all((symbol.isnumeric() and symbol != '0')
                 or symbol in (' ', '*') for symbol in line) and len(line) == 9):
            return False
    for row in board:
        row_nums = set()
        for elem in row:
            if elem.isdigit():
                if elem in row_nums:
                    return False
                row_nums.add(elem)
    for column in range(9):
        column_line = [line[column] for line in board]
        for symbol in column_line:
            if symbol.isnumeric() and column_line.count(symbol) > 1:
                return False
        color_line = column_line[:(9 - column)] + list(board[8 - column][(1 + column):])
        for symbol in color_line:
            if symbol.isnumeric() and color_line.count(symbol) > 1:
                return False
    return True
