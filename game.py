import ai
from classes import Board
from gui import (
    draw_board,
    draw_o_large,
    draw_o_small,
    draw_x_large,
    draw_x_small,
    draw_lines_thick,
    highlight_available_boards,
    draw_conclusion,
    get_mouse_pos
)

import pygame


def player_move(board_indexes: dict, selected_board, selected_column: int, selected_row: int, boardl):
    """
    Place x on selected section of full board

    Arguments:
    boardl -- full board
    board_indexes -- all sections of boardl mapped to their coordinates
    selected_board -- one of the sections of boardl
    selected_column -- column
    selected_row -- row
    """
    selected_board.place("x", selected_column % 3, selected_row % 3)
    draw_x_small(selected_row, selected_column)
    draw_lines_thick()

    place_full_on_large_board_player(
        selected_board, selected_column, selected_row, boardl
    )

    available_board_data = get_available_board_single(
        board_indexes, selected_row, selected_column
    )
    available_board = available_board_data[0]
    available_board_index = available_board_data[1]

    if selected_board.check_win():
        boardl.place("x", selected_column // 3, selected_row // 3)
        draw_x_large(selected_row // 3, selected_column // 3)
    if (
        available_board[0].is_available() is False
        or available_board[0].is_full() is True
    ):
        available_board_data = get_available_board_multiple(board_indexes)
        return available_board_data
    return available_board_index, available_board


def ai_move(board_indexes, boardl, available_board, available_board_index):
    """
    Place o on the board

    Arguments:
    boardl -- full board
    board_indexes -- all sections of boardl mapped to their coordinates
    available_board -- sections of boardl which are currently available
    available_board_index -- coordinates of boardl which are currently available
    """
    random_data = ai.choose_square_random(board_indexes, available_board_index)
    chosen_board_index = random_data[1]

    chosen_board = random_data[2]
    chosen_square = random_data[0]
    chosen_column = chosen_square[1]
    chosen_row = chosen_square[0]
    chosen_board.place("o", chosen_column, chosen_row)

    place_full_on_large_board_ai(chosen_board, chosen_board_index, boardl)

    draw_o_small(
        (chosen_board_index[0] * 3 + chosen_square[0]),
        (chosen_board_index[1] * 3 + chosen_square[1]),
    )
    available_board_index = chosen_square
    available_board = [board_indexes[available_board_index]]

    if chosen_board.check_win():
        boardl.place("o", chosen_board_index[1], chosen_board_index[0])
        draw_o_large(chosen_board_index[0], chosen_board_index[1])
    if (
        available_board[0].is_available() is False
        or available_board[0].is_full() is True
    ):
        available_board_data = get_available_board_multiple(board_indexes)
        return available_board_data
    return available_board_index, available_board


def place_full_on_large_board_player(selected_board, selected_column, selected_row, boardl):
    """
    Place f on full board if a section is full after player move

    Arguments:
    boardl -- full board
    selected_board -- section of full board
    selected_column -- column
    selected_row -- row
    """
    if selected_board.is_full() and not selected_board.check_win():
        boardl.place("f", selected_column // 3, selected_row // 3)


def place_full_on_large_board_ai(chosen_board, chosen_board_index, boardl):
    """
    Place f on full board if a section is full after ai move

    Arguments:
    boardl -- full board
    selected_board -- section of full board
    selected_column -- column
    selected_row -- row
    """
    if chosen_board.is_full() and not chosen_board.check_win():
        boardl.place("f", chosen_board_index[1], chosen_board_index[0])


def check_conditions(selected_board, selected_column, selected_row, available_board):
    """
    Check if figure can be placed on a section of the full board

    Arguments:
    selected_board -- section of full board
    selected_column -- column
    selected_row -- row
    available_board -- all currently available boards
    """
    if (
        selected_board.square_is_available(
            selected_column % 3, selected_row % 3
        )
        and selected_board.is_available()
        and selected_board in available_board
        and not selected_board.is_full()
    ):
        return True
    return False


def get_available_board_single(board_indexes, selected_row, selected_column):
    """
    Get available section of full board if only one is available

    Arguments:
    board_indexes -- all sections of boardl mapped to their coordinates
    selected_row -- row
    selected_column -- column
    """
    available_board_index = (selected_row % 3, selected_column % 3)
    available_board = [board_indexes[available_board_index]]
    return available_board, available_board_index


def get_available_board_multiple(board_indexes):
    """
    Get available section of full board if more than one are available

    Arguments:
    board_indexes -- all sections of boardl mapped to their coordinates
    """
    available_board_index = [
        index
        for index in list(board_indexes.keys())
        if board_indexes[index].is_available()
        and not board_indexes[index].is_full()
    ]
    available_board = [board_indexes[index] for index in available_board_index]
    return available_board_index, available_board


def draw_available_boards(boardl, available_board_index):
    """
    Draws which sections of full board are available on screen

    Arguments:
    boardl -- full_board
    available_board_index -- coordinates of available sections
    """
    if not boardl.check_win():
        if isinstance(available_board_index, list):
            for index in available_board_index:
                highlight_available_boards(index[0], index[1])
        else:
            highlight_available_boards(
                available_board_index[0], available_board_index[1]
            )


def game(board_indexes, available_board, available_board_index, boardl, small_boards):
    """
    Single tick of the game

    Arguments:
    board_indexes -- all full board sections mapped to their coordinates
    available_board -- currently available board sections
    available_board_index -- coordinates of currently available board sections
    boardl -- full board
    small_boards -- all sections of full board
    """
    mouse_pos = get_mouse_pos()
    selected_row = mouse_pos[0]
    selected_column = mouse_pos[1]
    selected_board = board_indexes[(selected_row // 3, selected_column // 3)]

    if check_conditions(
        selected_board, selected_column, selected_row, available_board
    ):

        available_board_data = player_move(
            board_indexes,
            selected_board,
            selected_column,
            selected_row,
            boardl,
        )
        available_board_index = available_board_data[0]
        available_board = available_board_data[1]

        if boardl.check_win():
            draw_conclusion("x")

        if not boardl.check_win() and not boardl.is_full():
            available_board_data = ai_move(
                board_indexes, boardl, available_board, available_board_index
            )
            available_board_index = available_board_data[0]
            available_board = available_board_data[1]
            draw_available_boards(boardl, available_board_index)

            if boardl.check_win():
                draw_conclusion("o")

    if boardl.check_win():
        for board in small_boards:
            available_board = []
            board.set_is_available(False)

    if boardl.is_full() is True and boardl.check_win() is False:
        draw_conclusion("draw")

    return available_board_index, available_board


def clear_boards(boardl, small_boards):
    """
    Clears full board and all sections

    Arguments:
    boardl -- full board
    small_boards -- full board sections
    """
    for board in small_boards:
        board.set_board([[0, 0, 0] for i in range(3)])
        board.set_is_available(True)
        board.set_is_full(False)
    boardl.set_board([[0, 0, 0] for i in range(3)])
    return small_boards, boardl


def restart_game(board_indexes, boardl):
    """
    Restart game

    Arguments:
    board_indexes -- all boards mapped to their coordinates on full board
    boardl -- full board
    """
    draw_board()
    available_board_index = list(board_indexes.keys())
    available_board = list(board_indexes.values())
    draw_available_boards(boardl, available_board_index)
    return available_board_index, available_board


def main():
    """Main game loop"""

    small_boards = [Board(name=i) for i in range(9)]
    boardl = Board()
    # store indexes for boards:
    board_indexes = {
        (0, 0): small_boards[0],
        (0, 1): small_boards[1],
        (0, 2): small_boards[2],
        (1, 0): small_boards[3],
        (1, 1): small_boards[4],
        (1, 2): small_boards[5],
        (2, 0): small_boards[6],
        (2, 1): small_boards[7],
        (2, 2): small_boards[8],
    }

    pygame.display.init()

    draw_board()

    available_board_index = list(board_indexes.keys())
    available_board = list(board_indexes.values())
    draw_available_boards(boardl, available_board_index)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                game_data = game(
                    board_indexes,
                    available_board,
                    available_board_index,
                    boardl,
                    small_boards,
                )
                available_board_index = game_data[0]
                available_board = game_data[1]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    new_boards = clear_boards(boardl, small_boards)
                    small_boards = new_boards[0]
                    boardl = new_boards[1]
                    available_board_data = restart_game(board_indexes, boardl)
                    available_board_index = available_board_data[0]
                    available_board = available_board_data[1]

                if event.key == pygame.K_q:
                    run = False

        pygame.display.update()


if __name__ == "__main__":
    main()
