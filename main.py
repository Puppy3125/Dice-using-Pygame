"""
Made by Puppy_3125 on Github
Github link: https://github.com/Puppy3125/Dice-using-Pygame
"""

import pygame, sys, random

print("Press the Space key for another roll!")

pygame.init()
screen = pygame.display.set_mode((500, 537))
d1 = pygame.image.load('image/i1.png')
d2 = pygame.image.load('image/i2.png')
d3 = pygame.image.load('image/i3.png')
d4 = pygame.image.load('image/i4.png')
d5 = pygame.image.load('image/i5.png')
d6 = pygame.image.load('image/i6.png')
icon1 = pygame.image.load('image/icon.png')
font = pygame.font.Font('font/font.ttf', 45)
text = font.render('Press space to roll again!', False, 'White')
text_rect = text.get_rect()
name_of_screen = pygame.display.set_caption("Dice")
icon = pygame.display.set_icon(icon1)
def main():
    screen.blit(text, (10, 6))
    def dice():
        rand = random.randint(1, 6)
        if rand == 1:
            screen.blit(d1, (0, 37))
        elif rand == 2:
            screen.blit(d2, (0, 37))
        elif rand == 3:
            screen.blit(d3, (0, 37))
        elif rand == 4:
            screen.blit(d4, (0, 37))
        elif rand == 5:
            screen.blit(d5, (0, 37))
        elif rand == 6:
            screen.blit(d6, (0, 37))
    dice()

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice()
main()
