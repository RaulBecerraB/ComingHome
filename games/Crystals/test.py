import pygame
import os
import math
import numpy as np

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Definir colores
BLACK = (0, 0, 0)
BROWN = (120, 60, 20)
YELLOW_START = (255, 200, 0)  # Amarillo más saturado
YELLOW_END = (255, 220, 50)  # Amarillo claro pero con mayor saturación
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class PuzzlePiece:
    def __init__(self, points, initial_position, highlight):
        self.points = points
        self.position = list(initial_position)  # Posición actual de la pieza
        self.placed = False
        self.dragging = False
        self.highlight = highlight

    def draw(self, surface):
        translated_points = [
            (
                point[0] + self.position[0] - 360,  # Centrar en la pantalla
                point[1] + self.position[1] - 360
            ) for point in self.points
        ]
        draw_realistic_triangle(surface, translated_points, self.highlight)

class HexPuzzleGame:
    def __init__(self, background_image_path=None, image_size=None):
        self.screen = pygame.display.set_mode((720, 720))
        pygame.display.set_caption("Rompecabezas Hexagonal")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.running = True
        self.selected_piece = None
        self.game_completed = False
        self.pieces = []
        self.correct_positions = []
        self.snap_distance = 50  # Distancia para encajar automáticamente
        self.correct_sound = generate_tone(frequency=523, duration_ms=300)
        
        # Cargar imagen de fondo si se proporciona una ruta
        self.background_image = None
        if background_image_path:
            self.load_background_image(background_image_path, image_size)

        self.setup_pieces()

    def load_background_image(self, path, size):
        """Cargar la imagen de fondo y centrarla en la pantalla según el tamaño proporcionado"""
        self.background_image = pygame.image.load(path)
        if size:
            self.background_image = pygame.transform.scale(self.background_image, size)
        
        # Calcular el offset para centrar la imagen
        image_width, image_height = size if size else self.background_image.get_size()
        self.image_offset_x = (720 - image_width) // 2
        self.image_offset_y = (720 - image_height) // 2

    def setup_pieces(self):
        center = (360, 360)
        radius = 150

        # Calcular posiciones correctas de los triángulos
        for i in range(6):
            angle1 = math.radians(60 * i)
            angle2 = math.radians(60 * (i + 1))
            point1 = center
            point2 = (center[0] + radius * math.cos(angle1), center[1] + radius * math.sin(angle1))
            point3 = (center[0] + radius * math.cos(angle2), center[1] + radius * math.sin(angle2))
            self.correct_positions.append((point1, point2, point3))

        # Crear piezas y definir posiciones iniciales
        for i in range(6):
            initial_position = (100 + i * 100, 100)
            highlight = i in [0, 1, 2, 3, 4, 5]  # Definir qué piezas tendrán brillo
            piece = PuzzlePiece(self.correct_positions[i], initial_position, highlight)
            self.pieces.append(piece)

    def run(self):
        while self.running:
            self.handle_events()
            self.update_display()
            self.clock.tick(60)
        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_completed:
                self.handle_mouse_down(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP and self.selected_piece:
                self.handle_mouse_up()
            elif event.type == pygame.MOUSEMOTION and self.selected_piece and self.selected_piece.dragging:
                self.handle_mouse_motion(event.pos)

    def handle_mouse_down(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        for piece in self.pieces:
            if not piece.placed:
                translated_points = [
                    (
                        point[0] + piece.position[0] - 360,
                        point[1] + piece.position[1] - 360
                    ) for point in piece.points
                ]
                if pygame.draw.polygon(self.screen, BLACK, translated_points).collidepoint(mouse_x, mouse_y):
                    self.selected_piece = piece
                    piece.dragging = True
                    self.offset_x_drag = mouse_x - piece.position[0]
                    self.offset_y_drag = mouse_y - piece.position[1]
                    break

    def handle_mouse_up(self):
        self.selected_piece.dragging = False
        correct_x, correct_y = self.correct_positions[self.pieces.index(self.selected_piece)][0]
        if abs(self.selected_piece.position[0] - correct_x) < self.snap_distance and abs(self.selected_piece.position[1] - correct_y) < self.snap_distance:
            self.selected_piece.position = [correct_x, correct_y]
            self.selected_piece.placed = True
            self.correct_sound.play()
        self.selected_piece = None

    def handle_mouse_motion(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        new_x = mouse_x - self.offset_x_drag
        new_y = mouse_y - self.offset_y_drag
        new_x = max(0, min(new_x, 720 - 100))
        new_y = max(0, min(new_y, 720 - 100))
        self.selected_piece.position = [new_x, new_y]

    def update_display(self):
        self.screen.fill(BLACK)
        
        # Dibujar imagen de fondo centrada si está presente
        if self.background_image:
            self.screen.blit(self.background_image, (self.image_offset_x, self.image_offset_y))

        # Dibujar molde del hexágono
        for i in range(6):
            pygame.draw.polygon(self.screen, GREEN, self.correct_positions[i], 1)

        # Dibujar las piezas
        all_pieces_placed = True
        for piece in self.pieces:
            piece.draw(self.screen)
            if not piece.placed:
                all_pieces_placed = False

        # Verificar si el juego se ha completado
        if all_pieces_placed and not self.game_completed:
            # text = self.font.render("¡Felicidades!", True, WHITE)
            # text_rect = text.get_rect(center=(360, 360))
            # self.screen.blit(text, text_rect)
            self.game_completed = True
            pygame.display.flip()
            pygame.time.delay(2000)
            self.running = False

        pygame.display.flip()

# Función para dibujar un triángulo con un efecto realista
def draw_realistic_triangle(surface, points, highlight):
    pygame.draw.polygon(surface, BROWN, points, 5)
    num_layers = 30
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
    pygame.draw.line(surface, BROWN, points[0], points[1], 2)
    pygame.draw.line(surface, BROWN, points[0], points[2], 2)
    pygame.draw.line(surface, BROWN, points[1], points[2], 2)

    if highlight:
        tip = points[0]
        base_midpoint = (
            (points[1][0] + points[2][0]) / 2,
            (points[1][1] + points[2][1]) / 2,
        )
        offset_tip = (tip[0] * 0.85 + base_midpoint[0] * 0.15, tip[1] * 0.85 + base_midpoint[1] * 0.15)
        pygame.draw.ellipse(surface, WHITE, (offset_tip[0] - 3, offset_tip[1] - 3, 6, 6))
        offset_base = (tip[0] * 0.3 + base_midpoint[0] * 0.7, tip[1] * 0.3 + base_midpoint[1] * 0.7)
        pygame.draw.ellipse(surface, WHITE, (offset_base[0] - 4, offset_base[1] - 4, 8, 8))

# Función para generar un tono de acierto
def generate_tone(frequency=440, duration_ms=300, volume=0.5):
    sample_rate = 44100
    samples = np.sin(2 * np.pi * np.arange(sample_rate * duration_ms / 1000) * frequency / sample_rate)
    samples = (samples * 32767).astype(np.int16)
    samples = np.repeat(samples[:, np.newaxis], 2, axis=1)
    sound = pygame.sndarray.make_sound(samples)
    sound.set_volume(volume)
    return sound

# Ejecutar el juego
if __name__ == "__main__":
    game = HexPuzzleGame(background_image_path="resources/hero-image.jpeg", image_size=(1080, 720))  # Cambia la ruta de la imagen y el tamaño deseado
    game.run()
