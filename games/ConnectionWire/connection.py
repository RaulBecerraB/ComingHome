import pygame
import random  # Importa la biblioteca random para desordenar la lista

# Inicializa pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 720, 720
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Juego de Conexión de Cables")

# Colores de los cables
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# Tamaño deseado para los sprites
SPRITE_SIZE = (40, 40)  

# Cargar imágenes de sprites para los cables
sprites = {
    'red': pygame.transform.scale(pygame.image.load('./asset/rojo.png'),SPRITE_SIZE),
    'green': pygame.transform.scale(pygame.image.load('./asset/rojo.png'),SPRITE_SIZE),
    'blue': pygame.transform.scale(pygame.image.load('./asset/rojo.png'),SPRITE_SIZE),
    'yellow': pygame.transform.scale(pygame.image.load('./asset/rojo.png'),SPRITE_SIZE),
    'purple': pygame.transform.scale(pygame.image.load('./asset/rojo.png'),SPRITE_SIZE)
}

# Fuente para mostrar el mensaje
font = pygame.font.SysFont(None, 40)

# Función para obtener posiciones ajustadas a la ventana
def get_positions(width, height):
    left_positions = [(int(width * 0.1), int(i * height / 6) + int(height * 0.1)) for i in range(5)]
    right_positions = [(int(width * 0.9), int(i * height / 6) + int(height * 0.1)) for i in range(5)]
    
    # Desordenar las posiciones de la izquierda
    random.shuffle(left_positions)
    
    return left_positions, right_positions

# Variables para arrastrar cables
dragging = False
current_cable = None
start_pos = None

# Lista para almacenar las conexiones correctas
correct_connections = []

# Obtener posiciones iniciales
left_positions, right_positions = get_positions(WIDTH, HEIGHT)

# Bucle principal del juego
running = True
show_correct_message = False
correct_message_time = 0  # Tiempo restante para mostrar el mensaje correcto

show_incorrect_message = False
incorrect_message_time = 0  # Tiempo restante para mostrar el mensaje incorrecto

while running:
    # Cambia el color de fondo
    window.fill((20, 20, 20))  # Fondo azul claro

    # Dibuja los puntos de conexión usando sprites
     # Dibuja los puntos de conexión usando sprites
    for i, color in enumerate(colors):
        if color == (255, 0, 0):
            window.blit(sprites['red'], (left_positions[i][0] - SPRITE_SIZE[0] // 2, left_positions[i][1] - SPRITE_SIZE[1] // 2))
            window.blit(sprites['red'], (right_positions[i][0] - SPRITE_SIZE[0] // 2, right_positions[i][1] - SPRITE_SIZE[1] // 2))
        elif color == (0, 255, 0):
            window.blit(sprites['green'], (left_positions[i][0] - SPRITE_SIZE[0] // 2, left_positions[i][1] - SPRITE_SIZE[1] // 2))
            window.blit(sprites['green'], (right_positions[i][0] - SPRITE_SIZE[0] // 2, right_positions[i][1] - SPRITE_SIZE[1] // 2))
        elif color == (0, 0, 255):
            window.blit(sprites['blue'], (left_positions[i][0] - SPRITE_SIZE[0] // 2, left_positions[i][1] - SPRITE_SIZE[1] // 2))
            window.blit(sprites['blue'], (right_positions[i][0] - SPRITE_SIZE[0] // 2, right_positions[i][1] - SPRITE_SIZE[1] // 2))
        elif color == (255, 255, 0):
            window.blit(sprites['yellow'], (left_positions[i][0] - SPRITE_SIZE[0] // 2, left_positions[i][1] - SPRITE_SIZE[1] // 2))
            window.blit(sprites['yellow'], (right_positions[i][0] - SPRITE_SIZE[0] // 2, right_positions[i][1] - SPRITE_SIZE[1] // 2))
        elif color == (255, 0, 255):
            window.blit(sprites['purple'], (left_positions[i][0] - SPRITE_SIZE[0] // 2, left_positions[i][1] - SPRITE_SIZE[1] // 2))
            window.blit(sprites['purple'], (right_positions[i][0] - SPRITE_SIZE[0] // 2, right_positions[i][1] - SPRITE_SIZE[1] // 2))

    # Dibuja las conexiones correctas almacenadas
    for connection in correct_connections:
        pygame.draw.line(window, connection['color'], connection['start'], connection['end'], 5)

    # Dibuja el cable mientras se arrastra
    if dragging and start_pos:
        pygame.draw.line(window, colors[current_cable], start_pos, pygame.mouse.get_pos(), 5)

    # Mostrar mensaje si la conexión es correcta
    if show_correct_message:
        text = font.render("¡Conexión correcta!", True, (0, 255, 0))
        window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT * 0.05))

        # Reducir el tiempo restante para mostrar el mensaje
        if correct_message_time > 0:
            correct_message_time -= 1
        else:
            show_correct_message = False  # Ocultar el mensaje cuando el tiempo se acabe

    # Mostrar mensaje si la conexión es incorrecta
    if show_incorrect_message:
        text = font.render("Conexión incorrecta", True, (255, 0, 0))
        window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT * 0.1))

        # Reducir el tiempo restante para mostrar el mensaje
        if incorrect_message_time > 0:
            incorrect_message_time -= 1
        else:
            show_incorrect_message = False  # Ocultar el mensaje cuando el tiempo se acabe

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            left_positions, right_positions = get_positions(WIDTH, HEIGHT)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, pos in enumerate(left_positions):
                if pygame.Rect(pos[0] - 20, pos[1] - 20, 40, 40).collidepoint(event.pos):
                    dragging = True
                    current_cable = i
                    start_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                for i, pos in enumerate(right_positions):
                    if pygame.Rect(pos[0] - 20, pos[1] - 20, 40, 40).collidepoint(event.pos):
                        if current_cable == i:  # Si el cable coincide
                            print("¡Conexión correcta!")
                            show_correct_message = True
                            correct_message_time = 120  # Mostrar mensaje por 2 segundos (60 FPS)
                            # Guardar la conexión correcta
                            correct_connections.append({
                                'color': colors[current_cable],
                                'start': start_pos,
                                'end': pos
                            })
                        else:
                            print("Conexión incorrecta.")
                            show_incorrect_message = True
                            incorrect_message_time = 120  # Mostrar mensaje por 2 segundos (60 FPS)
                dragging = False
                current_cable = None
                start_pos = None

    pygame.display.update()

pygame.quit()
