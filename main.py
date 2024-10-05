# import pygame
# import sys

# # Inicializa Pygame
# pygame.init()

# # Configura la pantalla
# screen_width, screen_height = 720, 720
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Desplazamiento de Imagen")

# # Carga la imagen grande
# image = pygame.image.load('fondo.png')  # Asegúrate de que la imagen tenga 720x3600
# image_rect = image.get_rect()

# # Variables para el desplazamiento
# scroll_x = 0
# scroll_speed = 5  # Velocidad de desplazamiento
# target_x = 0  # Posición de destino para el desplazamiento
# moving = False  # Estado de movimiento

# # Variables para la escena
# scene_width = 720
# current_scene = 1
# total_scenes = 3  # Número de escenas

# # Dimensiones del botón
# button_width, button_height = 150, 50

# # Crea un botón centrado
# button_rect = pygame.Rect(
#     (screen_width - button_width) // 2,  # Calcula la posición X para centrar
#     (screen_height - button_height) // 2,  # Calcula la posición Y para centrar
#     button_width, button_height
# )

# # Bucle principal
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN and not moving:  # Solo permite entrada si no está en movimiento
#             if event.key == pygame.K_LEFT:  # Tecla de flecha izquierda
#                 if current_scene > 1:
#                     target_x = max(0, scroll_x - scene_width)  # Mueve 720 píxeles a la izquierda
#                     current_scene -= 1
#                     moving = True
#             elif event.key == pygame.K_RIGHT:  # Tecla de flecha derecha
#                 if current_scene < total_scenes:
#                     target_x = min(image_rect.width - screen_width, scroll_x + scene_width)  # Mueve 720 píxeles a la derecha
#                     current_scene += 1
#                     moving = True
#         if event.type == pygame.MOUSEBUTTONDOWN and current_scene == 3:
#             if button_rect.collidepoint(event.pos):
#                 print("¡Botón clickeado!")

#     # Animación del desplazamiento
#     if moving:
#         if scroll_x < target_x:
#             scroll_x += scroll_speed
#             if scroll_x >= target_x:
#                 scroll_x = target_x
#                 moving = False  # Termina el movimiento
#         elif scroll_x > target_x:
#             scroll_x -= scroll_speed
#             if scroll_x <= target_x:
#                 scroll_x = target_x
#                 moving = False  # Termina el movimiento

#     # Dibuja la imagen desplazada
#     screen.blit(image, (-scroll_x, 0))

#     # Si estamos en la tercera escena, dibuja el botón centrado
#     if current_scene == 3:
#         pygame.draw.rect(screen, (255, 0, 0), button_rect)  # Dibuja el botón en rojo
#         font = pygame.font.SysFont(None, 24)
#         button_text = font.render('Botón', True, (255, 255, 255))
#         screen.blit(button_text, (button_rect.x + (button_width - button_text.get_width()) // 2,
#                                   button_rect.y + (button_height - button_text.get_height()) // 2))

#     # Actualiza la pantalla
#     pygame.display.flip()

# # Cierra Pygame
# pygame.quit()
# sys.exit()

# import pygame
# import sys
# import random
# import time
# import ComingHome.games.Simon.simon as SimonModule  # Asegúrate de que este sea el nombre correcto del módulo

# # Inicializa Pygame
# pygame.init()

# # Configura la pantalla
# screen_width, screen_height = 720, 720
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Desplazamiento de Imagen")

# # Carga la imagen grande
# image = pygame.image.load('fondo.png')  # Asegúrate de que la imagen tenga 720x3600
# image_rect = image.get_rect()

# # Variables para el desplazamiento
# scroll_x = 0
# scroll_speed = 5  # Velocidad de desplazamiento
# target_x = 0  # Posición de destino para el desplazamiento
# moving = False  # Estado de movimiento

# # Variables para la escena
# scene_width = 720
# current_scene = 1
# total_scenes = 3  # Número de escenas

# # Dimensiones del botón
# button_width, button_height = 150, 50

# # Crea un botón centrado
# button_rect = pygame.Rect(
#     (screen_width - button_width) // 2,  # Calcula la posición X para centrar
#     (screen_height - button_height) // 2,  # Calcula la posición Y para centrar
#     button_width, button_height
# )

# # Estado para el juego Simon
# simon_active = False
# show_button = False  # Nuevo estado para controlar la visibilidad del botón

# # Variables del juego Simon
# FPS = 60
# FLASHSPEED = 500
# FLASHDELAY = 200
# BUTTONSIZE = 100
# BUTTONGAPSIZE = 20
# TIMEOUT = 5

# BRIGHTRED = (255, 0, 0)
# BRIGHTGREEN = (0, 255, 0)
# BRIGHTBLUE = (0, 0, 255)
# BRIGHTYELLOW = (255, 255, 0)

# RED = (155, 0, 0)
# GREEN = (0, 155, 0)
# BLUE = (0, 0, 155)
# YELLOW = (155, 155, 0)
# bgColor = (0, 0, 0)

# XMARGIN = int((360 - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
# YMARGIN = int((360 - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

# YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
# BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
# REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
# GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

# def draw_buttons(surface):
#     pygame.draw.rect(surface, YELLOW, YELLOWRECT)
#     pygame.draw.rect(surface, BLUE, BLUERECT)
#     pygame.draw.rect(surface, RED, REDRECT)
#     pygame.draw.rect(surface, GREEN, GREENRECT)

# # Bucle principal
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if not simon_active:  # Solo permite entrada si Simon no está activo
#             if event.type == pygame.KEYDOWN and not moving:  # Solo permite entrada si no está en movimiento
#                 if event.key == pygame.K_LEFT:  # Tecla de flecha izquierda
#                     if current_scene > 1:
#                         target_x = max(0, scroll_x - scene_width)  # Mueve 720 píxeles a la izquierda
#                         current_scene -= 1
#                         moving = True
#                         show_button = False  # Oculta el botón durante el movimiento
#                 elif event.key == pygame.K_RIGHT:  # Tecla de flecha derecha
#                     if current_scene < total_scenes:
#                         target_x = min(image_rect.width - screen_width, scroll_x + scene_width)  # Mueve 720 píxeles a la derecha
#                         current_scene += 1
#                         moving = True
#                         show_button = False  # Oculta el botón durante el movimiento
#             if event.type == pygame.MOUSEBUTTONDOWN and current_scene == 3 and show_button:
#                 if button_rect.collidepoint(event.pos):
#                     simon_active = True  # Activa el juego Simon

#     # Animación del desplazamiento
#     if moving and not simon_active:
#         if scroll_x < target_x:
#             scroll_x += scroll_speed
#             if scroll_x >= target_x:
#                 scroll_x = target_x
#                 moving = False  # Termina el movimiento
#                 if current_scene == 3:  # Muestra el botón solo si estamos en la tercera escena
#                     show_button = True
#         elif scroll_x > target_x:
#             scroll_x -= scroll_speed
#             if scroll_x <= target_x:
#                 scroll_x = target_x
#                 moving = False  # Termina el movimiento
#                 if current_scene == 3:  # Muestra el botón solo si estamos en la tercera escena
#                     show_button = True

#     # Dibuja la imagen desplazada
#     screen.blit(image, (-scroll_x, 0))

#     # Si estamos en la tercera escena y no estamos moviendo, dibuja el botón centrado
#     if current_scene == 3 and not simon_active and show_button:
#         pygame.draw.rect(screen, (255, 0, 0), button_rect)  # Dibuja el botón en rojo
#         font = pygame.font.SysFont(None, 24)
#         button_text = font.render('Jugar Simon', True, (255, 255, 255))
#         screen.blit(button_text, (button_rect.x + (button_width - button_text.get_width()) // 2,
#                                   button_rect.y + (button_height - button_text.get_height()) // 2))

#     # Inicia el juego Simon si está activo
#     if simon_active and current_scene == 3:
#         simonSurface = pygame.Surface((360, 360))
#         simonSurface.fill(bgColor)  # Asegúrate de que el fondo del mini-juego sea visible
#         SimonModule.simon_game(simonSurface)  # Llama a la función del módulo Simon
#         screen.blit(simonSurface, (180, 180))  # Dibuja el juego Simon en el centro de la pantalla

#     # Actualiza la pantalla
#     pygame.display.flip()

# # Cierra Pygame
# pygame.quit()
# sys.exit()

# import pygame
# import sys
# import random
# import time
# import ComingHome.games.Simon.simon as SimonModule  # Asegúrate de que este sea el nombre correcto del módulo

# # Inicializa Pygame
# pygame.init()

# # Configura la pantalla
# screen_width, screen_height = 720, 720
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Desplazamiento de Imagen")

# # Carga la imagen grande
# image = pygame.image.load('fondo5.png')  # Asegúrate de que la imagen tenga 720x3600
# image_rect = image.get_rect()

# # Variables para el desplazamiento
# scroll_x = 0
# scroll_speed = 5  # Velocidad de desplazamiento
# target_x = 0  # Posición de destino para el desplazamiento
# moving = False  # Estado de movimiento

# # Variables para la escena
# scene_width = 720
# current_scene = 1
# total_scenes = 3  # Número de escenas

# # Dimensiones del botón
# button_width, button_height = 150, 50

# # Crea un botón centrado
# button_rect = pygame.Rect(
#     (screen_width - button_width) // 2,  # Calcula la posición X para centrar
#     (screen_height - button_height) // 2,  # Calcula la posición Y para centrar
#     button_width, button_height
# )

# # Estado para el juego Simon
# simon_active = False
# show_button = False  # Nuevo estado para controlar la visibilidad del botón

# # Variables del juego Simon
# FPS = 60
# FLASHSPEED = 500
# FLASHDELAY = 200
# BUTTONSIZE = 100
# BUTTONGAPSIZE = 20
# TIMEOUT = 5

# BRIGHTRED = (255, 0, 0)
# BRIGHTGREEN = (0, 255, 0)
# BRIGHTBLUE = (0, 0, 255)
# BRIGHTYELLOW = (255, 255, 0)

# RED = (155, 0, 0)
# GREEN = (0, 155, 0)
# BLUE = (0, 0, 155)
# YELLOW = (155, 155, 0)
# bgColor = (0, 0, 0)

# XMARGIN = int((360 - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
# YMARGIN = int((360 - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

# YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
# BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
# REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
# GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

# def draw_buttons(surface):
#     pygame.draw.rect(surface, YELLOW, YELLOWRECT)
#     pygame.draw.rect(surface, BLUE, BLUERECT)
#     pygame.draw.rect(surface, RED, REDRECT)
#     pygame.draw.rect(surface, GREEN, GREENRECT)

# # Bucle principal
# running = True
# game_running = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if not game_running:  # Solo permite entrada si Simon no está activo
#             if event.type == pygame.KEYDOWN and not moving:  # Solo permite entrada si no está en movimiento
#                 if event.key == pygame.K_LEFT:  # Tecla de flecha izquierda
#                     if current_scene > 1:
#                         target_x = max(0, scroll_x - scene_width)  # Mueve 720 píxeles a la izquierda
#                         current_scene -= 1
#                         moving = True
#                         show_button = False  # Oculta el botón durante el movimiento
#                 elif event.key == pygame.K_RIGHT:  # Tecla de flecha derecha
#                     if current_scene < total_scenes:
#                         target_x = min(image_rect.width - screen_width, scroll_x + scene_width)  # Mueve 720 píxeles a la derecha
#                         current_scene += 1
#                         moving = True
#                         show_button = False  # Oculta el botón durante el movimiento
#             if event.type == pygame.MOUSEBUTTONDOWN and current_scene == 3 and show_button:
#                 if button_rect.collidepoint(event.pos):
#                     game_running = True  # Activa el juego Simon

#     # Animación del desplazamiento
#     if moving and not game_running:
#         if scroll_x < target_x:
#             scroll_x += scroll_speed
#             if scroll_x >= target_x:
#                 scroll_x = target_x
#                 moving = False  # Termina el movimiento
#                 if current_scene == 3:  # Muestra el botón solo si estamos en la tercera escena
#                     show_button = True
#         elif scroll_x > target_x:
#             scroll_x -= scroll_speed
#             if scroll_x <= target_x:
#                 scroll_x = target_x
#                 moving = False  # Termina el movimiento
#                 if current_scene == 3:  # Muestra el botón solo si estamos en la tercera escena
#                     show_button = True

#     # Dibuja la imagen desplazada
#     screen.blit(image, (-scroll_x, 0))

#     # Si estamos en la tercera escena y no estamos moviendo, dibuja el botón centrado
#     if current_scene == 3 and not game_running and show_button:
#         pygame.draw.rect(screen, (255, 0, 0), button_rect)  # Dibuja el botón en rojo
#         font = pygame.font.SysFont(None, 24)
#         button_text = font.render('Jugar Simon', True, (255, 255, 255))
#         screen.blit(button_text, (button_rect.x + (button_width - button_text.get_width()) // 2,
#                                   button_rect.y + (button_height - button_text.get_height()) // 2))

#     # Inicia el juego Simon si está activo
#     if game_running and current_scene == 3:
#         # simonSurface = pygame.Surface((350, 350))
#         # simonSurface.fill(bgColor)  # Asegúrate de que el fondo del mini-juego sea visible
#         # SimonModule.simon_game(simonSurface)  # Llama a la función del módulo Simon
#         # screen.blit(simonSurface, (180, 180))  # Dibuja el juego Simon en el centro de la pantalla
        
#         # EJECUCION DEL JUEGO SIMON
#         SimonModule.start_game(pygame.display.set_mode((screen_width, screen_height)))  # Use the same surface for the game
#         game_running = False

#     # Actualiza la pantalla
#     pygame.display.flip()

# # Cierra Pygame
# pygame.quit()
# sys.exit()



import pygame
import sys
import random
import time
import games.Simon.simon as SimonModule  # Asegúrate de que este sea el nombre correcto del módulo

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen_width, screen_height = 720, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Comming Home")

# Carga la imagen grande
image = pygame.image.load('Escenario1_PIXEL.png')  # Asegúrate de que la imagen tenga 720x3600
image_rect = image.get_rect()

# Variables para el desplazamiento
scroll_x = 0
scroll_speed = 5  # Velocidad de desplazamiento
target_x = 0  # Posición de destino para el desplazamiento
moving = False  # Estado de movimiento

# Variables para la escena
scene_width = 720
current_scene = 1
total_scenes = 3  # Número de escenas

# Dimensiones del botón
button_width, button_height = 150, 50

# Crea un botón centrado
button_rect = pygame.Rect(
    (screen_width - button_width) // 2,  # Calcula la posición X para centrar
    (screen_height - button_height) // 2,  # Calcula la posición Y para centrar
    button_width, button_height
)

# Estado para el juego Simon
simon_active = False
show_button = False  # Nuevo estado para controlar la visibilidad del botón
move_after_game = False  # Estado para mover la pantalla después de Simon
move_start_time = 0  # Tiempo de inicio del movimiento

# Bucle principal
running = True
game_running = False

def ease_in_out(start, end, t):
    if t < 0.5:
        return start + (end - start) * (2 * t ** 2)
    else:
        t = t * 2 - 1
        return start + (end - start) * (1 - t * (t - 2))
    
def flash():
    # Tiempo de duración del efecto
    duration = 1  # 1 segundo
    start_time = time.time()

    while True:

        # Calcula el tiempo transcurrido
        elapsed_time = time.time() - start_time
        t = min(elapsed_time / duration, 1)  # Normaliza t entre 0 y 1

        # Crea una superficie blanca con opacidad
        opacity = int(ease_in_out(0, 255, t*2))  # Interpolación de opacidad
        white_surface = pygame.Surface((screen_width, screen_height))
        white_surface.fill((255, 255, 255))
        white_surface.set_alpha(opacity)  # Establece la opacidad

        # Dibuja en la pantalla
        screen.fill((0, 0, 0))  # Limpia la pantalla con negro
        screen.blit(white_surface, (0, 0))  # Dibuja la superficie blanca

        pygame.display.flip()  # Actualiza la pantalla

        # Termina si el tiempo ha pasado
        if t >= 1:
            break
    
        pygame.time.delay(20)

def photo():
    # Mostrar una foto en el canvas
    image = pygame.image.load('imgs/FirstDeepField.jpg')
    surface = pygame.display.set_mode((720,720))
    surface.blit(image, (0, 0))
    pygame.display.update()

    pygame.time.delay(3000)    


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_running:  # Solo permite entrada si Simon no está activo
            if event.type == pygame.KEYDOWN and not moving:  # Solo permite entrada si no está en movimiento
                if event.key == pygame.K_LEFT:  # Tecla de flecha izquierda
                    if current_scene > 1:
                        target_x = max(0, scroll_x - scene_width)  # Mueve 720 píxeles a la izquierda
                        current_scene -= 1
                        moving = True
                        show_button = False  # Oculta el botón durante el movimiento
                elif event.key == pygame.K_RIGHT:  # Tecla de flecha derecha
                    if current_scene < total_scenes:
                        target_x = min(image_rect.width - screen_width, scroll_x + scene_width)  # Mueve 720 píxeles a la derecha
                        current_scene += 1
                        moving = True
                        show_button = False  # Oculta el botón durante el movimiento
            if event.type == pygame.MOUSEBUTTONDOWN and current_scene == 3 and show_button:
                if button_rect.collidepoint(event.pos):
                    game_running = True  # Activa el juego Simon

    # Animación del desplazamiento
    if moving and not game_running:
        if scroll_x < target_x:
            scroll_x += scroll_speed
            if scroll_x >= target_x:
                scroll_x = target_x
                moving = False  # Termina el movimiento
                if current_scene == 3:  # Muestra el botón solo si estamos en la tercera escena
                    show_button = True
        elif scroll_x > target_x:
            scroll_x -= scroll_speed
            if scroll_x <= target_x:
                scroll_x = target_x
                moving = False  # Termina el movimiento
                if current_scene == 3:  # Muestra el botón solo si estamos en la tercera escena
                    show_button = True

    # Dibuja la imagen desplazada
    screen.blit(image, (-scroll_x, 0))

    # Si estamos en la tercera escena y no estamos moviendo, dibuja el botón centrado
    if current_scene == 3 and not game_running and show_button:
        pygame.draw.rect(screen, (255, 0, 0), button_rect)  # Dibuja el botón en rojo
        font = pygame.font.SysFont(None, 24)
        button_text = font.render('Jugar Simon', True, (255, 255, 255))
        # screen.blit(button_text, (button_rect.x + (button_width - button_text.get_width()) // 2,
        #                           button_rect.y + (button_height - button_text.get_height()) // 2))
        pygame.draw.rect(screen, "RED", button_rect)

    # Inicia el juego Simon si está activo
    if game_running and current_scene == 3:
        SimonModule.start_game(pygame.display.set_mode((screen_width, screen_height)))  # Use the same surface for the game
        game_running = False
        show_button = False
        move_after_game = True  # Activa el movimiento después del juego Simon
        move_start_time = pygame.time.get_ticks()  # Guarda el tiempo actual

    # Mueve la pantalla hacia la derecha después del juego Simon
    if move_after_game:
        if scroll_x < image_rect.width - screen_width:
            scroll_x += scroll_speed - 2 
            
        else:
            move_after_game = False  # Detiene el movimiento
            pygame.time.delay(1000)
            flash()
            photo()
            
    
    

    # Actualiza la pantalla
    
    pygame.display.flip()


# Cierra Pygame
pygame.quit()
sys.exit()
