import unittest

from puzzle_ai import validate_board

class TestValidateBoard(unittest.TestCase):
    def test_valid_board(self):
        # Valid board
        valid_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 1****",
            "     9 5 ",
            " 6  83  *",
            "3   2  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertTrue(validate_board(valid_board))

    def test_invalid_board(self):
        # Invalid board (two 1s in the fifth column)
        invalid_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 9****",
            "     9 5 ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertFalse(validate_board(invalid_board))

    def test_columns_valid(self):
        # Valid board with unique digits in each column
        valid_columns_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 1****",
            "     9 5 ",
            " 6  83  *",
            "3   2  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertTrue(validate_board(valid_columns_board))

    def test_columns_invalid(self):

        # Invalid board with duplicate digits in the first column
        invalid_columns_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 1****",
            "     9 5 ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertFalse(validate_board(invalid_columns_board))

    def test_color_blocks_valid(self):
        # Valid board with unique digits in all color blocks
        valid_color_blocks_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 1****",
            "     9 5 ",
            " 6  83  *",
            "3   2  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertTrue(validate_board(valid_color_blocks_board))

    def test_color_blocks_invalid(self):
        # Invalid board with duplicate digits in the second color block
        invalid_color_blocks_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 1****",
            "     9 5 ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2  ****"
        ]
        self.assertFalse(validate_board(invalid_color_blocks_board))

    def test_empty_board(self):
        empty_board = ["*********"] * 9
        self.assertTrue(validate_board(empty_board))

    def test_invalid_zero(self):
        invalid_row_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 1****",
            "     9 5 ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2  ****0"  # Invalid row with digit 0
        ]
        self.assertFalse(validate_board(invalid_row_board))

    def test_invalid_board_size(self):
        # Valid board
        valid_board = [
            "**** ****",
            "***1 ****",
            "**  3****",
            "* 4 1****",
            "     9 5 ",
            " 6  83  *",
            "3   2  **",
            "  8  2**",
            "  2  ****"
        ]
        self.assertFalse(validate_board(valid_board))


if __name__ == "__main__":
    unittest.main()
