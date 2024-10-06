import pygame
import random
import os

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
background = pygame.image.load("games/AsteroidDestroyer/assets/images/space_PIXELEADO.png")

# Clase para los asteroides
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("games/AsteroidDestroyer/assets/images/Asteroide_PIXELEADO.png").convert_alpha()  # Cargar imagen del asteroide
        self.image = pygame.transform.scale(self.original_image, (150, 150))  # Redimensionar la imagen del asteroide
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = 100
        self.speed_y = random.randint(3, 8)  # Asteroides más lentos
        self.bounced = False

    def update(self):
        self.rect.y += self.speed_y
        # Verificar si el asteroide llega al fondo de la pantalla
        if self.rect.bottom >= screen_height:
            self.speed_y = -self.speed_y  # Invertir la dirección para que rebote hacia arriba
        # Verificar si el asteroide llega al tope de la pantalla después de rebotar
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y  # Invertir la dirección para que rebote hacia abajo

           
# Grupo de sprites
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

# Función para crear un nuevo asteroide
def create_asteroid():
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Crear asteroides iniciales con posiciones fijas en x
fixed_positions_x = [0, 130, 280, 430, 580]  # Posiciones fijas en x para los asteroides
for i in range(5):  # Menos asteroides
    asteroid = Asteroid()
    asteroid.rect.x = fixed_positions_x[i]
    all_sprites.add(asteroid)
    asteroids.add(asteroid)
    
# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in asteroids if s.rect.collidepoint(pos)]
            for asteroid in clicked_sprites:
                # Cargar sonidos
                sound_folder = "games/AsteroidDestroyer/assets/sounds/"
                sound_files = [os.path.join(sound_folder, f) for f in os.listdir(sound_folder) if f.endswith('.wav')]
                sounds = [pygame.mixer.Sound(sound_file) for sound_file in sound_files]

                # Reproducir un sonido aleatorio
                random.choice(sounds).play()
                asteroid.kill()
            #    create_asteroid()

    all_sprites.update()
    screen.blit(background, (0, 0))  # Dibujar la imagen de fondo
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()