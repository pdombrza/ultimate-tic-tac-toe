from classes import Board
from ai import choose_board_random, choose_square_random
from ai import NoBoardToChooseFromError
import pytest


def test_create_board():
    boards = Board()
    assert boards.board() == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_is_full():
    boards = Board()
    assert boards.is_full() is False


def test_is_full2():
    boards = Board()
    new_board = [
        ['x', 0, 'x'],
        [0, 'x', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.is_full() is False


def test_is_full3():
    boards = Board()
    new_board = [
        ['x', 'x', 'x'],
        [0, 'x', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.is_full() is False
    assert boards.is_available() is False


def test_is_full_full():
    boards = Board()
    new_board = [
        ['x', 'o', 'x'],
        ['o', 'x', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.is_full() is True
    assert boards.is_available() is False


def test_set_board():
    boards = Board()
    new_board = [
        ['x', 'o', 'x'],
        ['o', 'x', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.board() == new_board


def test_available_square():
    boards = Board()
    assert boards.square_is_available(1, 1) is True


def test_available_square2():
    boards = Board()
    new_board = [
        [0, 'o', 'x'],
        ['o', 'x', 0],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.square_is_available(column=0, row=0) is True
    assert boards.square_is_available(column=0, row=1) is False
    assert boards.square_is_available(column=0, row=2) is False
    assert boards.square_is_available(column=2, row=1) is True


def test_available_square_unavailable():
    boards = Board()
    new_board = [
        ['x', 'o', 'x'],
        ['o', 'x', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.square_is_available(1, 1) is False


def test_place():
    boards = Board()
    boards.place('x', 1, 1)
    assert boards.board() == [[0, 0, 0], [0, 'x', 0], [0, 0, 0]]


def test_place_full():
    boards = Board()
    new_board = [
        ['x', 'o', 'x'],
        [0, 'x', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.is_full() is False
    boards.place('o', 0, 1)
    assert boards.is_full() is True


def test_place_not_available():
    boards = Board()
    new_board = [
        ['x', 'o', 'x'],
        ['o', 'x', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    boards.place('x', 1, 1)
    boards.place('x', 1, 2)
    assert boards.board() == new_board


def test_check_win_rows():
    boards = Board()
    new_board = [
        ['x', 0, 'x'],
        ['o', 'o', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win_rows() is True


def test_check_win_rows_no_winner():
    boards = Board()
    new_board = [
        ['x', 0, 'x'],
        ['o', 0, 'o'],
        ['o', 0, 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win_rows() is False


def test_check_win_columns():
    boards = Board()
    new_board = [
        ['o', 0, 'x'],
        ['o', 0, 'o'],
        ['o', 0, 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win_columns() is True


def test_check_win_columns_no_winner():
    boards = Board()
    new_board = [
        ['o', 'x', 'x'],
        [0, 0, 'o'],
        ['o', 0, 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win_columns() is False


def test_check_win_diagonals():
    boards = Board()
    new_board = [
        ['o', 0, 'x'],
        [0, 'o', 'o'],
        ['o', 0, 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win_diagonals() is True


def test_check_win_diagonals2():
    boards = Board()
    new_board = [
        [0, 0, 'x'],
        [0, 'x', 'o'],
        ['x', 0, 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win_diagonals() is True


def test_check_win_diagonals_no_winner():
    boards = Board()
    new_board = [
        [0, 0, 'x'],
        [0, 0, 'o'],
        ['x', 0, 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win_diagonals() is False


def test_check_win_no_winner():
    boards = Board()
    new_board = [
        ['o', 0, 0],
        [0, 'x', 0],
        [0, 0, 0]
        ]
    boards.set_board(new_board)
    assert boards.check_win() is False
    assert boards.is_available() is True


def test_check_win():
    boards = Board()
    new_board = [
        ['o', 'o', 'x'],
        ['o', 0, 'x'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win() is True
    assert boards.is_full() is False
    assert boards.is_available() is False


def test_check_win_large():
    boards = Board()
    new_board = [
        ['o', 'o', 'x'],
        ['o', 'x', 'x'],
        ['f', 'f', 'f']
        ]
    boards.set_board(new_board)
    assert boards.check_win() is False
    assert boards.is_full() is True


def test_check_win_large2():
    boards = Board()
    new_board = [
        ['o', 'o', 'f'],
        ['o', 'f', 'x'],
        ['f', 'f', 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win() is False
    assert boards.is_full() is True


def test_check_win_large3():
    boards = Board()
    new_board = [
        ['o', 'f', 'o'],
        ['o', 'f', 'x'],
        ['f', 'f', 'o']
        ]
    boards.set_board(new_board)
    assert boards.check_win() is False
    assert boards.is_full() is True


def test_check_win_large4():
    boards = Board()
    new_board = [
        ['f', 'f', 'f'],
        ['f', 'f', 'f'],
        ['f', 'f', 'f']
        ]
    boards.set_board(new_board)
    assert boards.check_win() is False
    assert boards.is_full() is True


def test_board_is_avaliable_not_available():
    boards = Board()
    new_board = [
        ['x', 'x', 'x'],
        ['o', 'o', 'o'],
        ['o', 'x', 'o']
        ]
    boards.set_board(new_board)
    assert boards.is_available() is False


def test_board_is_avaliable_not_available2():
    boards = Board()
    new_board = [
        ['o', 'o', 'x'],
        ['o', 0, 'x'],
        ['o', 'x', 'o']
    ]
    boards.set_board(new_board)
    assert boards.is_available() is False


def test_board_is_avaliable_not_available3():
    boards = Board()
    new_board = [
        ['o', 'o', 'x'],
        ['x', 0, 'x'],
        ['o', 'x', 'o']
    ]
    boards.set_board(new_board)
    assert boards.is_available() is True


def test_set_board_empty():
    boards = Board()
    new_board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    boards.set_board(new_board)
    assert boards.is_full() is False
    assert boards.is_available() is True


def test_choose_square_random(monkeypatch):
    boards = Board()
    new_board = [[0, 0, 0], [0, "x", 0], [0, "o", "o"]]

    board_indexes = {(1, 2): boards}

    def mock_square(t):
        return (1, 2)

    boards.set_board(new_board)
    monkeypatch.setattr("ai.choice", mock_square)
    assert choose_square_random(board_indexes, list(board_indexes.keys())) == (
        (1, 2),
        (1, 2),
        boards,
    )


def test_choose_square_random2():
    boards = Board()
    new_board = [[0, "x", "x"], ["x", "o", "x"], ["x", "o", "o"]]

    board_indexes = {(0, 0): boards}

    boards.set_board(new_board)
    assert choose_square_random(board_indexes, list(board_indexes.keys())) == (
        (0, 0),
        (0, 0),
        boards,
    )


def test_choose_board_random(monkeypatch):
    boards = [Board(name=i) for i in range(3)]
    new_board = [[0, "o", "x"], ["x", "x", "o"], ["o", "x", "x"]]

    for board in boards:
        board.set_board(new_board)

    board_indexes = {
        (0, 0): boards[0],
        (0, 1): boards[1],
        (0, 2): boards[2],
    }

    def mock_board(f):
        return (0, 1)

    monkeypatch.setattr("ai.choice", mock_board)

    assert choose_board_random(board_indexes, list(board_indexes.keys())) == (
        boards[1],
        (0, 1),
    )


def test_choose_board_no_boards_to_choose_from():
    boards = [Board(name=i) for i in range(3)]
    new_board = [[0, "o", "x"], ["x", "x", "o"], ["o", "x", "x"]]

    for board in boards:
        board.set_board(new_board)

    board_indexes = {
        (0, 0): boards[0],
        (0, 1): boards[1],
        (0, 2): boards[2],
    }

    available_board = []
    with pytest.raises(NoBoardToChooseFromError):
        choose_board_random(board_indexes, available_board)
