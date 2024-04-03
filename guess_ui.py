# pip/pip3 install pygame
import pygame
import random
import sys

pygame.init()
screen =pygame.display.set_mode((500, 500))
pygame.display.set_caption('Guess the Number Game')
font = pygame.font.Font(None, 36)
number_to_guess = random.randint(1, 10)
guess = None
attempts = 0
running = True

def display_message(message):
    text = font.render(message, True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (50, 150))
    pygame.display.flip()

while running or attempts < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: guess = 1
            elif event.key == pygame.K_2: guess = 2
            elif event.key == pygame.K_3: guess = 3
            elif event.key == pygame.K_4: guess = 4
            elif event.key == pygame.K_5: guess = 5
            elif event.key == pygame.K_6: guess = 6
            elif event.key == pygame.K_7: guess = 7
            elif event.key == pygame.K_8: guess = 8
            elif event.key == pygame.K_9: guess = 9
            elif event.key == pygame.K_0: guess = 10
            attempts += 1
            if guess < number_to_guess: display_message('Pick a Higher Number!')
            elif guess > number_to_guess: display_message('Pick a Lower Number!')
            else:
                display_message(f'Correct! Attempts: {attempts}')
                running = False

            pygame.time.wait(2000)
            pygame.display.flip()
            screen.fill((255, 255, 255))    

pygame.quit()
sys.exit()