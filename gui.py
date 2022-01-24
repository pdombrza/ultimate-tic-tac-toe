import pygame


WIDTH = 720
MARGIN = int(0.014 * WIDTH)
WHITE = (255, 250, 250)
LINEWIDTH_THIN = 5
LINEWIDTH_THICK = 10
FIGUREWIDTH_THIN = 5
FIGUREWIDTH_THICK = 10
BORDERWIDTH = 2
SQUARE_SIZE = int((WIDTH - 6 * LINEWIDTH_THIN - 4 * LINEWIDTH_THICK) / 9)
BLACK = (0, 0, 0)
SILVER = (169, 169, 169)
RED = (255, 51, 51)
BLUE = (51, 51, 255)
GREEN = (127, 255, 0)
BG_COLOR = WHITE
FONT_SIZE = int(WIDTH / 28)
FONT = "dejavusansmono"

SCREEN = pygame.display.set_mode((WIDTH, WIDTH))


def draw_lines_thin():
    for i in range(1, 9):
        pygame.draw.line(
            SCREEN,
            SILVER,
            (i * (WIDTH / 9), MARGIN),
            (i * (WIDTH / 9), WIDTH - MARGIN),
            LINEWIDTH_THIN,
        )
        pygame.draw.line(
            SCREEN,
            SILVER,
            (MARGIN, i * WIDTH / 9),
            (WIDTH - MARGIN, i * WIDTH / 9),
            LINEWIDTH_THIN,
        )


def draw_lines_thick():
    for i in range(1, 3):
        pygame.draw.line(
            SCREEN,
            BLACK,
            (i * (WIDTH / 3), MARGIN),
            (i * (WIDTH / 3), WIDTH - MARGIN),
            LINEWIDTH_THICK,
        )
        pygame.draw.line(
            SCREEN,
            BLACK,
            (MARGIN, i * (WIDTH / 3)),
            (WIDTH - MARGIN, i * (WIDTH / 3)),
            LINEWIDTH_THICK,
        )
    pygame.draw.rect(
        SCREEN, BLACK, (0, 0, WIDTH, WIDTH), width=LINEWIDTH_THICK
    )


def draw_x_large(row, column):
    pygame.draw.line(
        SCREEN,
        RED,
        (2 * MARGIN + (WIDTH / 3) * column, 2 * MARGIN + (WIDTH / 3) * row),
        (
            ((WIDTH / 3) - 2 * MARGIN) + (WIDTH / 3) * column,
            ((WIDTH / 3) - 2 * MARGIN) + (WIDTH / 3) * row,
        ),
        FIGUREWIDTH_THICK,
    )
    pygame.draw.line(
        SCREEN,
        RED,
        (
            2 * MARGIN + (WIDTH / 3) * column,
            ((WIDTH / 3) - 2 * MARGIN) + (WIDTH / 3) * row,
        ),
        (
            ((WIDTH / 3) - 2 * MARGIN) + (WIDTH / 3) * column,
            2 * MARGIN + (WIDTH / 3) * row,
        ),
        FIGUREWIDTH_THICK,
    )


def draw_x_small(row, column):
    pygame.draw.line(
        SCREEN,
        RED,
        (
            (MARGIN + SQUARE_SIZE / 4.8) + (WIDTH / 9) * column,
            (MARGIN + SQUARE_SIZE / 4.8) + (WIDTH / 9) * row,
        ),
        (
            (WIDTH / 9 - (MARGIN / 2 + SQUARE_SIZE / 4.8))
            + (WIDTH / 9) * column,
            (WIDTH / 9 - (MARGIN / 2 + SQUARE_SIZE / 4.8)) + (WIDTH / 9) * row,
        ),
        width=FIGUREWIDTH_THIN,
    )
    pygame.draw.line(
        SCREEN,
        RED,
        (
            (MARGIN + SQUARE_SIZE / 4.8) + (WIDTH / 9) * column,
            (WIDTH / 9 - (MARGIN / 2 + SQUARE_SIZE / 4.8)) + (WIDTH / 9) * row,
        ),
        (
            (WIDTH / 9 - (MARGIN / 2 + SQUARE_SIZE / 4.8))
            + (WIDTH / 9) * column,
            (MARGIN + SQUARE_SIZE / 4.8) + (WIDTH / 9) * row,
        ),
        width=FIGUREWIDTH_THIN,
    )


def draw_o_large(row, column):
    pygame.draw.circle(
        SCREEN,
        BLUE,
        ((WIDTH / 6) + (WIDTH / 3) * column, WIDTH / 6 + (WIDTH / 3) * row),
        radius=(WIDTH / 6 - 2 * MARGIN),
        width=FIGUREWIDTH_THICK,
    )


def draw_o_small(row, column):
    pygame.draw.circle(
        SCREEN,
        BLUE,
        (
            SQUARE_SIZE / 2 + MARGIN / 2 + (WIDTH / 9) * column,
            SQUARE_SIZE / 2 + MARGIN / 2 + (WIDTH / 9) * row,
        ),
        radius=(SQUARE_SIZE / 2 - 2 * MARGIN / 2),
        width=FIGUREWIDTH_THIN,
    )


def get_mouse_pos():
    """Get mouse position"""
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    selected_row = int(mouse_y // (WIDTH // 9))
    selected_column = int(mouse_x // (WIDTH // 9))
    return selected_row, selected_column


def highlight_available_boards(board_index_x, board_index_y):
    """Highlight available boards"""
    pygame.draw.rect(
        SCREEN,
        GREEN,
        (
            (((WIDTH / 3) - BORDERWIDTH) * board_index_y + MARGIN / 2),
            (((WIDTH / 3) - BORDERWIDTH) * board_index_x + MARGIN / 2),
            (WIDTH / 3) - MARGIN / 2 + BORDERWIDTH,
            (WIDTH / 3) - MARGIN / 2 + BORDERWIDTH,
        ),
        BORDERWIDTH,
    )


def draw_conclusion(winner):
    """Display winner on screen"""
    pygame.font.init()
    rectangle = pygame.draw.rect(
        SCREEN, WHITE, (0, 0, WIDTH, (SQUARE_SIZE / 2))
    )
    if winner == "draw":
        text = "Draw, press r to restart, press q to quit"
    else:
        text = f"Winner: {winner}, press r to restart, press q to quit"
    text_object = pygame.font.SysFont(FONT, FONT_SIZE).render(
        text, True, BLACK
    )
    text_rectangle = text_object.get_rect(center=rectangle.center)
    SCREEN.blit(text_object, text_rectangle)


def draw_board():
    """Draw game board"""
    pygame.display.set_caption("Ultimate Tic Tac Toe")
    SCREEN.fill(BG_COLOR)
    draw_lines_thin()
    draw_lines_thick()
