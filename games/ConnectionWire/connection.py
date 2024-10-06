import pygame
import random

class CableConnectionGame:
    def __init__(self, width=720, height=720):
        # Inicializa pygame
        pygame.init()

        # Configuración de la ventana
        self.WIDTH, self.HEIGHT = width, height
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
    
        self.background_image = pygame.image.load('fondo5FRAME.png')  # Cambia la ruta a tu imagen
        # self.window.blit(self.background_image, (0, 0))

        # Colores de los cables
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

        # Tamaño de los puntos pixelados
        self.PIXEL_SIZE = 40
        self.LINE_PIXEL_SIZE = 15  # Tamaño de los "píxeles" de la línea de conexión

        # Variables para arrastrar cables
        self.dragging = False
        self.current_cable = None
        self.start_pos = None

        # Lista para almacenar las conexiones correctas
        self.correct_connections = []

        # Obtener posiciones iniciales
        self.left_positions, self.right_positions = self.get_positions(self.WIDTH, self.HEIGHT)
        
        self.score = 0

    # Función para obtener posiciones ajustadas a la ventana
    def get_positions(self, width, height):
        left_positions = [(int(width * 0.1)+125, int(i * height / 10) + int(height * 0.1) + 225) for i in range(5)]
        right_positions = [(int(width * 0.9)-125, int(i * height / 10) + int(height * 0.1) + 225) for i in range(5)]
        random.shuffle(left_positions)  # Desordenar las posiciones de la izquierda
        return left_positions, right_positions

    # Función para dibujar una "línea pixelada" entre dos puntos
    def draw_pixelated_line(self, screen, color, start_pos, end_pos, pixel_size):
        # Calcula la distancia entre los puntos de inicio y fin
        distance = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5
        num_pixels = int(distance // pixel_size)

        for i in range(num_pixels):
            # Interpolación lineal para obtener posiciones a lo largo de la línea
            t = i / num_pixels
            x = int(start_pos[0] * (1 - t) + end_pos[0] * t)
            y = int(start_pos[1] * (1 - t) + end_pos[1] * t)

            # Dibuja un rectángulo más grande en esa posición para simular una línea gruesa
            pygame.draw.rect(screen, color, (x, y, pixel_size, pixel_size))

    # Función principal para ejecutar el juego
    def run(self):
        running = True
        while running:
            self.window.blit(self.background_image, (0, 0))
            # Cambia el color de fondo
            # self.window.fill((20, 20, 20))  # Fondo oscuro

            # Dibuja los puntos de conexión usando colores pixelados
            for i, color in enumerate(self.colors):
                # Dibuja puntos en la izquierda
                pygame.draw.rect(self.window, color, 
                                (self.left_positions[i][0] - self.PIXEL_SIZE // 2, 
                                self.left_positions[i][1] - self.PIXEL_SIZE // 2, 
                                self.PIXEL_SIZE, self.PIXEL_SIZE))
                # Dibuja puntos en la derecha
                pygame.draw.rect(self.window, color, 
                                (self.right_positions[i][0] - self.PIXEL_SIZE // 2, 
                                self.right_positions[i][1] - self.PIXEL_SIZE // 2, 
                                self.PIXEL_SIZE, self.PIXEL_SIZE))

            # Dibuja las conexiones correctas almacenadas
            for connection in self.correct_connections:
                self.draw_pixelated_line(self.window, connection['color'], connection['start'], connection['end'], self.LINE_PIXEL_SIZE)

            # Dibuja el cable mientras se arrastra
            if self.dragging and self.start_pos:
                # Ajusta la posición del inicio de la línea al centro del cuadrado
                adjusted_start = (self.start_pos[0] + self.PIXEL_SIZE // 2, self.start_pos[1] + self.PIXEL_SIZE // 2)
                self.draw_pixelated_line(self.window, self.colors[self.current_cable], adjusted_start, pygame.mouse.get_pos(), self.LINE_PIXEL_SIZE)

            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if event.type == pygame.VIDEORESIZE:
                #     self.WIDTH, self.HEIGHT = event.w, event.h
                #     self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
                #     self.left_positions, self.right_positions = self.get_positions(self.WIDTH, self.HEIGHT)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, pos in enumerate(self.left_positions):
                        if pygame.Rect(pos[0] - self.PIXEL_SIZE // 2, pos[1] - self.PIXEL_SIZE // 2, self.PIXEL_SIZE, self.PIXEL_SIZE).collidepoint(event.pos):
                            self.dragging = True
                            self.current_cable = i
                            self.start_pos = pos

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.dragging:
                        for i, pos in enumerate(self.right_positions):
                            if pygame.Rect(pos[0] - self.PIXEL_SIZE // 2, pos[1] - self.PIXEL_SIZE // 2, self.PIXEL_SIZE, self.PIXEL_SIZE).collidepoint(event.pos):
                                if self.current_cable == i:  # Si el cable coincide
                                    # print("¡Conexión correcta!")
                                    # Ajusta las posiciones de inicio y fin de las conexiones correctas al centro de los cuadrados
                                    self.score += 1
                                    self.correct_connections.append({
                                        'color': self.colors[self.current_cable],
                                        'start': (self.start_pos[0] - self.PIXEL_SIZE // 2, self.start_pos[1] - self.PIXEL_SIZE // 2),
                                        'end': (pos[0] - self.PIXEL_SIZE // 2, pos[1] - self.PIXEL_SIZE // 2)
                                    })
                                # else:
                                #     print("Conexión incorrecta.")
                        self.dragging = False
                        self.current_cable = None
                        self.start_pos = None

            pygame.display.update()
            if self.score == 5:
                return

        pygame.quit()

# Este código permite que el juego sea llamado desde otro programa
if __name__ == "__main__":
    game = CableConnectionGame()
    game.run()
