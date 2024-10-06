import pygame
import sys
import numpy as np
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 720
HEIGHT = 720
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = (WIDTH - 200) // BOARD_COLS 
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = pygame.Color('black')
LINE_COLOR = pygame.Color('#9FFB97')
CIRCLE_COLOR = pygame.Color('#3CE342')
CROSS_COLOR = pygame.Color('#1A7E1E')

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (164, SQUARE_SIZE + 135), (WIDTH - 165, SQUARE_SIZE + 135), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (164, 2 * SQUARE_SIZE + 42), (WIDTH - 165, 2 * SQUARE_SIZE  + 42), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE + 50, 250), (SQUARE_SIZE + 50, HEIGHT -75), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE - 50, 250), (2 * SQUARE_SIZE - 50, HEIGHT-75), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS - 20, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return not np.any(board == 0)

def check_win(player):
    # Vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # Horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # Ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # Descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), LINE_WIDTH)

def draw_asc_diagonal(player):
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)

def draw_desc_diagonal(player):
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)

def restart():
    screen.fill(BG_COLOR)
    # draw_lines()
    board.fill(0)


def tictactoe():
    # draw_lines()
    # Main loop
    player = 1
    game_over = False
    bot_won = False
    draw_game = False
    winner_time = 0
    bot_move_time = 0  # Tiempo para el movimiento del bot
    bot_turn_pending = False  # Bandera para indicar si el movimiento del bot está pendiente

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if not bot_won and not draw_game and game_over:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 1:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                        winner_time = time.time()  # Registrar el tiempo del ganador
                    elif is_board_full():
                        game_over = True
                        draw_game = True
                        winner_time = time.time()  # Registrar el tiempo del empate

                    player = player % 2 + 1
                    draw_figures()

                    # Preparar el movimiento del bot
                    if not game_over and player == 2:
                        bot_turn_pending = True
                        bot_move_time = time.time() + 0.5  # Bot hará su movimiento en 1 segundo

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    game_over = False
                    bot_won = False
                    draw_game = False
                    bot_turn_pending = False

        # Movimiento del bot después del retraso de 1 segundo
        if bot_turn_pending and time.time() >= bot_move_time:
            bot_turn_pending = False
            # Movimiento del bot
            available = np.argwhere(board == 0)
            if len(available) > 0:
                choice = random.choice(available)
                mark_square(choice[0], choice[1], 2)
                if check_win(2):
                    game_over = True
                    bot_won = True  # Registrar si el bot ganó
                    winner_time = time.time()  # Registrar el tiempo del ganador
                elif is_board_full():
                    game_over = True
                    draw_game = True
                    winner_time = time.time()  # Registrar el tiempo del empate

                player = player % 2 + 1
                draw_figures()

        # Verificar si ha pasado el tiempo después de que el bot gane o haya empate para reiniciar el juego
        if (bot_won or draw_game) and (time.time() - winner_time) > 1:
            restart()
            game_over = False
            bot_won = False
            draw_game = False
            bot_turn_pending = False

        pygame.display.update()
