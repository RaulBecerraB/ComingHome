import pygame

class TorresHanoi:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.tower_height = 260  # Altura de las torres
        self.tower_positions = [(180, height - self.tower_height), (360, height - self.tower_height), (540, height - self.tower_height)]
        
        # Definición de los discos, ajustando sus tamaños
        self.disks = [
            {'width': 130, 'height': 30, 'color': (0, 0, 255), 'tower': 0, 'y_offset': 0},
            {'width': 90, 'height': 30, 'color': (0, 255, 0), 'tower': 0, 'y_offset': 0},
            {'width': 50, 'height': 30, 'color': (255, 0, 0), 'tower': 0, 'y_offset': 0}
        ]
        self.selected_tower = None

    def draw(self):
        # Dibujar el fondo negro
        self.screen.fill((0, 0, 0))

        # Dibujar las torres (blancas)
        for pos in self.tower_positions:
            pygame.draw.rect(self.screen, (255, 255, 255), (pos[0] - 5, 200, 8, self.tower_height))

        # Dibujar los discos
        towers = {0: [], 1: [], 2: []}
        for disk in self.disks:
            towers[disk['tower']].append(disk)
        for tower_index, tower in enumerate(towers.values()):
            for i, disk in enumerate(tower):
                tower_x = self.tower_positions[tower_index][0]
                # Ajustar la posición Y para los discos
                y = self.height - (i + 1) * disk['height'] - 250  # Ajustar para centrar mejor los discos
                disk['y_offset'] = y
                pygame.draw.rect(self.screen, disk['color'], (tower_x - disk['width'] // 2, y, disk['width'], disk['height']))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            clicked_tower = None
            for i, pos in enumerate(self.tower_positions):
                if abs(mouse_x - pos[0]) < 50:
                    clicked_tower = i
                    break

            if clicked_tower is not None:
                if self.selected_tower is None:
                    self.selected_tower = clicked_tower
                else:
                    origin_tower = self.selected_tower
                    destination_tower = clicked_tower
                    origin_disks = [disk for disk in self.disks if disk['tower'] == origin_tower]

                    if origin_disks:
                        disk_to_move = min(origin_disks, key=lambda d: d['width'])
                        smaller_disks = [disk for disk in self.disks if disk['tower'] == destination_tower]
                        # Comprobar si el movimiento es válido
                        if not smaller_disks or disk_to_move['width'] < min(smaller_disks, key=lambda d: d['width'])['width']:
                            disk_to_move['tower'] = destination_tower
                        else:
                            # Reiniciar el juego si el movimiento es inválido
                            self.reset_game()
                    self.selected_tower = None

    def is_complete(self):
        return all(disk['tower'] == 2 for disk in self.disks)

    def reset_game(self):
        # Reiniciar las torres y los discos
        for disk in self.disks:
            disk['tower'] = 0  # Colocar todos los discos en la torre 0
        self.selected_tower = None

# Verificar si este archivo es ejecutado directamente
if __name__ == "__main__":
    pygame.init()

    WIDTH, HEIGHT = 720, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Torres de Hanoi")

    # Crear instancia de TorresHanoi
    torres_hanoi = TorresHanoi(screen, WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pasar los eventos al juego
            torres_hanoi.handle_event(event)

        # Dibujar el juego
        torres_hanoi.draw()

        # Verificar si el juego está completo
        if torres_hanoi.is_complete():
            # Reiniciar el juego si se completa
            torres_hanoi.reset_game()

        # Actualizar pantalla
        pygame.display.update()

    pygame.quit()
