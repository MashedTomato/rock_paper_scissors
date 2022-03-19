###
# Rock paper scissors game loop
###

###import block
import pygame
import sys
import gamePieces
import choice
###

# initializing pygame
pygame.init()
c_size = 256
c_number = 5

# Draws the window
screen = pygame.display.set_mode(
    (c_size * c_number, c_size * c_number))

# Sets the caption of the window
pygame.display.set_caption('Rock, Paper, Scissors')


# Initializing game piece classes
rock = gamePieces.Rock()
paper = gamePieces.Paper()
scissors = gamePieces.Scissors()
game_choice = choice.Choice()

clock = pygame.time.Clock()

#SCREEN_UPDATE = PYGAME.USEREVENT
#PYGAME.TIME.SET_TIMER(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # setting screen color
    screen.fill((220, 220, 200))

    # Drawing game pieces
    rock.draw_rock(c_size, screen)
    paper.draw_paper(c_size, screen)
    scissors.draw_scissors(c_size, screen)
    if rock.is_clicked() == True:
        game_choice.game_choice(1)

    elif paper.is_clicked() == True:
        game_choice.game_choice(2)

    elif scissors.is_clicked() == True:
        game_choice.game_choice(3)

    game_choice.draw_choice(c_size, screen)
    # refreshing the screen

    # clock.tick(120)
    pygame.display.update()
