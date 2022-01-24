class Board:
    """
    Class Board. Contains attributes:

    :param name: board name, defaults to empty string
    :type name: str
    :param is_available: board availability, defaults to True
    :type is_available: bool
    :param is_full: board fullness, defaults to False
    :type is_full: bool
    """

    def __init__(self, name="", is_available=True, is_full=False):
        self._board = [[0, 0, 0] for index in range(3)]
        self.name = name
        self._is_available = is_available
        self._is_full = is_full

    def board(self):
        return self._board

    def set_board(self, new_board):
        self._board = new_board
        if self.is_full() and not self.check_win():
            self.set_is_full(True)
            self.set_is_available(False)
        elif self.check_win() and self.is_full():
            self.set_is_full(True)
            self.set_is_available(False)
        elif self.check_win() and not self.is_full():
            self.set_is_full(False)
            self.set_is_available(False)
        else:
            self.set_is_full(False)
            self.set_is_available(True)

    def is_available(self):
        return self._is_available

    def set_is_available(self, new_is_available):
        self._is_available = new_is_available

    def is_full(self):
        for i, row in enumerate(self.board()):
            for j, column in enumerate(self.board()):
                if self.board()[i][j] == 0:
                    return False
        return True

    def set_is_full(self, full):
        self._is_full = full

    def square_is_available(self, column, row):
        return self.board()[row][column] == 0

    def place(self, char, column, row):
        if self.square_is_available(column, row) and self.is_available():
            self._board[row][column] = char
        if self.is_full():
            self.set_is_full(True)

    def check_win_rows(self):
        for row in self._board:
            if len(set(row)) == 1 and row[0] != 0 and row[0] != "f":
                return True
        return False

    def check_win_columns(self):
        board = self.board()
        for i in range(3):
            if (
                board[0][i] == board[1][i] == board[2][i]
                and board[0][i] != 0
                and board[0][i] != "f"
            ):
                return True
        return False

    def check_win_diagonals(self):
        board = self.board()
        diagonal1 = [board[i][i] for i in range(3)]
        diagonal2 = [board[i][2 - i] for i in range(3)]
        if (
            len(set(diagonal1)) == 1
            and diagonal1[0] != 0
            and diagonal1[0] != "f"
            or len(set(diagonal2)) == 1
            and diagonal2[0] != 0
            and diagonal2[0] != "f"
        ):
            return True
        return False

    def check_win(self):
        if (
            self.check_win_rows()
            or self.check_win_diagonals()
            or self.check_win_columns()
        ):
            self.set_is_available(False)
            return True
        return False
