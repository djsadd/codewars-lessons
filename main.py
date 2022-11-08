import pygame

pygame.init()
pygame.display.set_caption("2048")
pygame.display.set_icon(pygame.image.load('icon2.png'))
screen = pygame.display.set_mode((600, 400))

clock = pygame.time.Clock()
FPS = 60

pygame.draw.rect(screen, (255, 255, 255), (10, 10, 50, 100), 2)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)