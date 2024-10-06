import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 720, 720
BORDER = 165  # Espacio de los bordes
LINE_WIDTH = 13
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = (WIDTH - 2 * BORDER) // BOARD_ROWS

# Desplazamiento vertical (en píxeles)
VERTICAL_OFFSET = 85

# Colores
WHITE = (255, 255, 255)
GREEN = pygame.Color('#9FFB97')
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Cargar imagen de fondo
background_img = pygame.image.load("fondo5FRAMEALIEN.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Tablero (3x3)
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Turno del jugador (True = jugador humano, False = máquina)
player_turn = True

# Dibujar el tablero
def draw_board():
    screen.blit(background_img, (0, 0))
    # Dibujar las líneas horizontales y verticales
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, GREEN, (BORDER, BORDER + row * SQUARE_SIZE + VERTICAL_OFFSET), 
                         (WIDTH - BORDER, BORDER + row * SQUARE_SIZE + VERTICAL_OFFSET), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, GREEN, (BORDER + col * SQUARE_SIZE, BORDER + VERTICAL_OFFSET), 
                         (BORDER + col * SQUARE_SIZE, HEIGHT - BORDER + VERTICAL_OFFSET), LINE_WIDTH)

# Dibujar X y O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                # Dibujar X
                pygame.draw.line(screen, RED, 
                                 (BORDER + col * SQUARE_SIZE + 20, BORDER + row * SQUARE_SIZE + 20 + VERTICAL_OFFSET), 
                                 (BORDER + (col + 1) * SQUARE_SIZE - 20, BORDER + (row + 1) * SQUARE_SIZE - 20 + VERTICAL_OFFSET), 
                                 LINE_WIDTH)
                pygame.draw.line(screen, RED, 
                                 (BORDER + (col + 1) * SQUARE_SIZE - 20, BORDER + row * SQUARE_SIZE + 20 + VERTICAL_OFFSET), 
                                 (BORDER + col * SQUARE_SIZE + 20, BORDER + (row + 1) * SQUARE_SIZE - 20 + VERTICAL_OFFSET), 
                                 LINE_WIDTH)
            elif board[row][col] == 'O':
                # Dibujar O
                pygame.draw.circle(screen, BLUE, 
                                   (BORDER + col * SQUARE_SIZE + SQUARE_SIZE // 2, BORDER + row * SQUARE_SIZE + SQUARE_SIZE // 2 + VERTICAL_OFFSET), 
                                   SQUARE_SIZE // 2 - 20, LINE_WIDTH)

# Verificar si alguien ganó
def check_winner():
    # Filas, columnas y diagonales
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# Verificar si el tablero está lleno
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

# Movimiento de la IA (aleatorio)
def ai_move():
    time.sleep(0.5)  # Pausa de 0.5 segundos
    available_moves = [(r, c) for r in range(BOARD_ROWS) for c in range(BOARD_COLS) if board[r][c] is None]
    if available_moves:
        move = random.choice(available_moves)
        board[move[0]][move[1]] = 'O'

# Reiniciar el tablero
def reset_board():
    global board, player_turn
    board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
    player_turn = True

# Juego principal
def play():
    global player_turn
    game_over = False
    winner = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
                mouseX, mouseY = event.pos
                clicked_row = (mouseY - BORDER - VERTICAL_OFFSET) // SQUARE_SIZE
                clicked_col = (mouseX - BORDER) // SQUARE_SIZE

                if 0 <= clicked_row < BOARD_ROWS and 0 <= clicked_col < BOARD_COLS:
                    if board[clicked_row][clicked_col] is None:
                        board[clicked_row][clicked_col] = 'X'
                        player_turn = False

        if not player_turn and not game_over:
            ai_move()
            player_turn = True

        # Dibujar todo
        # draw_board()
        screen.blit(background_img, (0, 0))
        draw_figures()


        pygame.display.update()
        winner = check_winner()
        if winner is not None:
            game_over = True
            if winner == 'X':
                return
            else:
                time.sleep(1)  # Si la IA gana, pausa de 1 segundo antes de reiniciar
                reset_board()
                game_over = False
        elif is_board_full():
            game_over = True
            time.sleep(1)  # Pausa de 1 segundo antes de reiniciar si hay empate
            reset_board()
            game_over = False

if __name__ == "__main__":
    play()
