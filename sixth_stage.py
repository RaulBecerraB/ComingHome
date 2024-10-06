import pygame
import sys
import random
import time
import games.Hannoi.hannoi as HannoiModule
from PIL import Image


def sixth_stage_main():
    
    # Inicializa Pygame
    pygame.init()

    # Configura la pantalla
    screen_width, screen_height = 720, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Comming Home")

    # Carga la imagen grande
    image = pygame.image.load('Escenario6_PIXEL.png')  # Asegúrate de que la imagen tenga 720x3600
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
    button_width, button_height = 50, 50

    # Crea un botón centrado
    button_rect = pygame.Rect(
        (screen_width - button_width) // 2,  # Calcula la posición X para centrar
        (screen_height - button_height) // 2,  # Calcula la posición Y para centrar
        button_width, button_height
    )

    # Estado para el juego Cristal
    cristal_active = False
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

    def extract_frames(gif_path):
        # Abrir el GIF usando Pillow
        gif = Image.open(gif_path)
        
        frames = []
        
        try:
            while True:
                # Convertir cada frame a un formato compatible con Pygame
                frame = gif.copy().convert('RGBA')
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()

                # Crear superficie de Pygame a partir del frame
                pygame_frame = pygame.image.fromstring(data, size, mode)
                frames.append(pygame_frame)

                # Avanzar al siguiente frame
                gif.seek(gif.tell() + 1)
        
        except EOFError:
            # Se alcanzó el final del GIF
            pass

        return frames

    def photo():
        # Inicializa Pygame
        pygame.init()

        # Crear la ventana
        surface = pygame.display.set_mode((720, 720))

        # Extraer los frames del GIF
        frames = extract_frames('imgs/TarantulaNebula.gif')

        # Variables de animación
        frame_index = 0
        clock = pygame.time.Clock()
        running = True
        paused = False  # Bandera para saber si la animación está en pausa (detenida)
        alpha = 0  # Nivel de opacidad inicial para el fade in
        fade_in_duration = 60  # Duración del fade in en frames (1 segundo si tienes 60 FPS)
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Revisar si se presiona la barra espaciadora
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if paused:
                        running = False  # Cerrar la aplicación al presionar la barra espaciadora si la animación está pausada

            # Limpiar la pantalla
            surface.fill((0, 0, 0))  # Cambia el color de fondo si es necesario
            
            # Obtener el frame actual
            frame = frames[frame_index].copy()

            # Aplicar fade in al inicio
            if alpha < 255:
                alpha = min(alpha + (255 // fade_in_duration), 255)
            frame.set_alpha(alpha)

            # Dibujar el frame con la opacidad aplicada
            surface.blit(frame, (0, 0))

            if not paused:  # Solo avanzar el frame si la animación no está en pausa
                # Actualizar el frame si no estamos en el último
                if frame_index < len(frames) - 1:
                    frame_index += 1
                else:
                    paused = True  # Detener la animación en el último frame

            # Actualizar la pantalla
            pygame.display.update()

            # Controlar la velocidad de la animación (FPS)
            clock.tick(60)  # Puedes ajustar la velocidad de la animación aquí

        # Salir de Pygame
        # second_stage.second_stage_main()
        pygame.quit()
        sys.exit()

    pygame.mixer.init()

    # Cargar la música de fondo
    pygame.mixer.music.load('Sounds/BaseSol.wav')

    # Reproducir la música en bucle (-1 para bucle infinito)
    pygame.mixer.music.play(loops=-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_running:  # Solo permite entrada si Simon no está activo
                if event.type == pygame.KEYDOWN and not moving:  # Solo permite entrada si no está en movimiento
                    if event.key == pygame.K_LEFT:  # Tecla de flecha izquierda
                        if current_scene > 1:
                            
                            # Cargar y reproducir el sonido Giro.mp3 en un canal separado
                            giro_sound = pygame.mixer.Sound('Sounds/Giro.mp3')
                            giro_channel = pygame.mixer.Channel(1)  # Asigna el sonido a un canal específico
                            giro_channel.play(giro_sound)
                            
                            # Movimiento de la imagen a la izquierda
                            
                            target_x = max(0, scroll_x - scene_width)  # Mueve 720 píxeles a la izquierda
                            current_scene -= 1
                            moving = True
                            show_button = False  # Oculta el botón durante el movimiento
                            
                    elif event.key == pygame.K_RIGHT:  # Tecla de flecha derecha
                        if current_scene < total_scenes:
                            
                            # Cargar y reproducir el sonido Giro.mp3 en un canal separado
                            giro_sound = pygame.mixer.Sound('Sounds/Giro.mp3')
                            giro_channel = pygame.mixer.Channel(1)  # Asigna el sonido a un canal específico
                            giro_channel.play(giro_sound)
                            
                            # Movimiento de la imagen a la derecha
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
            pygame.mixer.music.set_volume(0.5)  
            HannoiModule.play()
            # SimonModule.start_game(pygame.display.set_mode((screen_width, screen_height)))  # Use the same surface for the game
            pygame.mixer.music.set_volume(1)
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
                pygame.mixer.music.pause()
                camera_sound = pygame.mixer.Sound('Sounds/camera_flash.mp3')
                camera_channel = pygame.mixer.Channel(2)  # Asigna el sonido a un canal específico
                camera_channel.play(camera_sound)
                pygame.mixer.music.load('Sounds/06.mp3')

                # Reproducir la música en bucle (-1 para bucle infinito)
                pygame.mixer.music.play(loops=-1)
                flash()
                photo()
                
        
        

        # Actualiza la pantalla
        
        pygame.display.flip()


    # Cierra Pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    sixth_stage_main()