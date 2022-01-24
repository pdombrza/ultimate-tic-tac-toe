from random import choice


class NoBoardToChooseFromError(Exception):
    def __init__(self):
        super().__init__('No boards to choose from')


def choose_board_random(small_boards: dict, available_board):
    """
    Choose random section from available sections on full board

    Arguments:
    small_boards -- all sections
    available_board -- available sections
    """
    if not available_board:
        raise NoBoardToChooseFromError
    if isinstance(available_board, list):
        chosen_index = choice(available_board)
        chosen_board = small_boards[chosen_index]
    else:
        chosen_index = available_board
        chosen_board = small_boards[chosen_index]
    return chosen_board, chosen_index


def choose_square_random(small_boards: dict, available_board):
    """
    Choose random square from available squares in section

    Arguments:
    small_boards -- all sections
    available_board -- available sections
    """
    chosen_board_data = choose_board_random(small_boards, available_board)
    chosen_board = chosen_board_data[0]
    chosen_board_index = chosen_board_data[1]
    available_squares = []
    for i in range(3):
        for j in range(3):
            if chosen_board.square_is_available(i, j):
                available_squares.append((j, i))
    chosen_square = choice(available_squares)
    return chosen_square, chosen_board_index, chosen_board
