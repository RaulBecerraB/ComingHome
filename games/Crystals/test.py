import pygame
import os
import math

# Inicializar Pygame
pygame.init()

# Definir la resolución de la ventana (720 x 720)
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Rompecabezas Hexagonal")

# Definir colores
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
YELLOW_START = (255, 223, 0)  
YELLOW_END = (255, 235, 50)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Tamaño del hexágono
center = (360, 360)
radius = 150
snap_distance = 50  # Aumentar la distancia para encajar la pieza automáticamente

# Definir las posiciones correctas de las piezas (centro y vértices)
correct_positions = []

for i in range(6):
    # Calculamos los ángulos para obtener los vértices
    angle1 = math.radians(60 * i)
    angle2 = math.radians(60 * (i + 1))

    # Puntos del triángulo
    point1 = center
    point2 = (center[0] + radius * math.cos(angle1), center[1] + radius * math.sin(angle1))
    point3 = (center[0] + radius * math.cos(angle2), center[1] + radius * math.sin(angle2))

    # Guardar la posición correcta del triángulo
    correct_positions.append((point1, point2, point3))

# Piezas iniciales fuera del hexágono
pieces = []

for i in range(6):
    # Posición inicial fuera del hexágono para cada pieza
    piece = {
        "points": correct_positions[i],  # Los puntos del triángulo
        "position": [100 + i * 100, 100],  # Posición inicial arbitraria para cada triángulo
        "placed": False,  # Estado de la pieza
        "dragging": False  # Estado de arrastre
    }
    pieces.append(piece)

# Fuente para el mensaje de "Tarea Completada"
font = pygame.font.Font(None, 74)

# Función para dibujar un triángulo con un efecto de cristal
def draw_crystal_triangle(surface, points):
    # Dibujar el borde marrón oscuro con un grosor más pequeño
    pygame.draw.polygon(surface, BROWN, points, 5)

    # Crear un gradiente en el triángulo (dividiendo en capas)
    num_layers = 20
    for i in range(num_layers):
        ratio = i / num_layers
        color = (
            int(YELLOW_START[0] * (1 - ratio) + YELLOW_END[0] * ratio),
            int(YELLOW_START[1] * (1 - ratio) + YELLOW_END[1] * ratio),
            int(YELLOW_START[2] * (1 - ratio) + YELLOW_END[2] * ratio)
        )
        layer_points = [
            (
                points[0][0] * (1 - ratio) + points[1][0] * ratio,
                points[0][1] * (1 - ratio) + points[1][1] * ratio
            ),
            (
                points[0][0] * (1 - ratio) + points[2][0] * ratio,
                points[0][1] * (1 - ratio) + points[2][1] * ratio
            ),
            points[0]
        ]
        pygame.draw.polygon(surface, color, layer_points)

    # Dibujar destellos blancos para simular el reflejo de luz dentro del triángulo
    # Posicionar los destellos dentro del área del triángulo
    tip = points[0]
    base_midpoint = (
        (points[1][0] + points[2][0]) / 2,
        (points[1][1] + points[2][1]) / 2,
    )
    # Posicionar un destello cerca del vértice superior
    offset_tip = (
        tip[0] * 0.85 + base_midpoint[0] * 0.15,
        tip[1] * 0.85 + base_midpoint[1] * 0.15,
    )
    pygame.draw.ellipse(surface, WHITE, (offset_tip[0] - 5, offset_tip[1] - 5, 10, 10))

    # Posicionar otro destello en el centro del triángulo, un poco más hacia la base
    offset_base = (
        tip[0] * 0.3 + base_midpoint[0] * 0.7,
        tip[1] * 0.3 + base_midpoint[1] * 0.7,
    )
    pygame.draw.ellipse(surface, WHITE, (offset_base[0] - 7, offset_base[1] - 7, 14, 14))

# Bucle principal del juego
running = True
selected_piece = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for piece in pieces:
                if not piece["placed"]:
                    # Crear un polígono con los puntos de la pieza
                    translated_points = [
                        (
                            point[0] + piece["position"][0] - center[0],
                            point[1] + piece["position"][1] - center[1]
                        ) for point in piece["points"]
                    ]
                    if pygame.draw.polygon(screen, BLACK, translated_points).collidepoint(mouse_x, mouse_y):
                        # Marcar la pieza como seleccionada para arrastrar
                        selected_piece = piece
                        piece["dragging"] = True
                        offset_x_drag = mouse_x - piece["position"][0]
                        offset_y_drag = mouse_y - piece["position"][1]
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_piece:
                selected_piece["dragging"] = False
                # Verificar si la pieza está cerca de la posición correcta
                correct_x, correct_y = correct_positions[pieces.index(selected_piece)][0]
                if abs(selected_piece["position"][0] - correct_x) < snap_distance and abs(selected_piece["position"][1] - correct_y) < snap_distance:
                    # Encajar la pieza automáticamente en la posición correcta
                    selected_piece["position"] = [correct_x, correct_y]
                    selected_piece["placed"] = True
                selected_piece = None
        elif event.type == pygame.MOUSEMOTION:
            if selected_piece and selected_piece["dragging"]:
                mouse_x, mouse_y = event.pos
                new_x = mouse_x - offset_x_drag
                new_y = mouse_y - offset_y_drag

                # Restringir los movimientos para que no se salga de la pantalla
                new_x = max(0, min(new_x, 720 - 100))
                new_y = max(0, min(new_y, 720 - 100))

                selected_piece["position"] = [new_x, new_y]

    # Rellenar la pantalla con negro
    screen.fill(BLACK)

    # Dibujar el hexágono en su posición correcta (para referencia)
    for i in range(6):
        pygame.draw.polygon(screen, GREEN, correct_positions[i], 1)

    # Dibujar las piezas del hexágono con efecto cristal
    all_pieces_placed = True
    for piece in pieces:
        translated_points = [
            (
                point[0] + piece["position"][0] - center[0],
                point[1] + piece["position"][1] - center[1]
            ) for point in piece["points"]
        ]

        # Dibujar el triángulo con efecto cristal
        draw_crystal_triangle(screen, translated_points)

        if not piece["placed"]:
            all_pieces_placed = False

    # Verificar si todas las piezas han sido colocadas
    if all_pieces_placed:
        # Dibujar el mensaje de "Tarea Completada"
        text = font.render("¡Felicidades!", True, WHITE)
        text_rect = text.get_rect(center=(360, 360))
        screen.blit(text, text_rect)

        # Actualizar la pantalla y esperar 2 segundos antes de cerrar
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Cerrar Pygame
pygame.quit()
