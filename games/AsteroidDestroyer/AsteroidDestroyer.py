import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 720
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroid Destroyer")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Cargar imagen de fondo
background = pygame.image.load("./assets/space.jpg")

# Clase para los asteroides
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])  # Asteroides más grandes
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(1, 3)  # Asteroides más lentos

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            global game_over
            game_over = True

# Grupo de sprites
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

# Función para crear un nuevo asteroide
def create_asteroid():
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Crear asteroides iniciales
for i in range(3):  # Menos asteroides
    create_asteroid()
    
# Bucle principal del juego
running = True
game_over = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in asteroids if s.rect.collidepoint(pos)]
            for asteroid in clicked_sprites:
                asteroid.kill()
                create_asteroid()  # Crear un nuevo asteroide cuando uno es destruido

    if not game_over:
        all_sprites.update()

    screen.blit(background, (0, 0))  # Dibujar la imagen de fondo
    all_sprites.draw(screen)
    
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()