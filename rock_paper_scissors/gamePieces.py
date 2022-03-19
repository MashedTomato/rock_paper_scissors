###
# stores the classes for the game objects
###

# Import block
import pygame
###


class Rock:
    def __init__(self):
        self.rock = pygame.image.load('graphics/rock.png')

    def draw_rock(self, size, screen):
        self.rock_rect = pygame.Rect(size, size, size, size)
        screen.blit(self.rock, self.rock_rect)

    # Method to check for a click on one of the game pieces
    def is_clicked(self):
        # Gives true only if the game piece has been clicked on and the mouse has been released
        if pygame.mouse.get_pressed()[0] and self.rock_rect.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    return True
                else:
                    return False
        else:
            return False


class Paper:
    def __init__(self):
        self.paper = pygame.image.load('graphics/paper.png')

    def draw_paper(self, size, screen):
        self.paper_rect = pygame.Rect(size * 3, size, size, size)
        screen.blit(self.paper, self.paper_rect)

    # Method to check for a click on one of the game pieces
    def is_clicked(self):
        if pygame.mouse.get_pressed()[0] and self.paper_rect.collidepoint(pygame.mouse.get_pos()):
            # Gives true only if the game piece has been clicked on and the mouse has been released
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    return True
                else:
                    return False
        else:
            return False


class Scissors:
    def __init__(self):
        self.scissors = pygame.image.load('graphics/scissors.png')

    def draw_scissors(self, size, screen):
        self.scissors_rect = pygame.Rect(size * 2, size * 3, size, size)
        screen.blit(self.scissors, self.scissors_rect)

    # Method to check for a click on one of the game pieces
    def is_clicked(self):
        # Gives true only if the game piece has been clicked on and the mouse has been released
        if pygame.mouse.get_pressed()[0] and self.scissors_rect.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    return True
                else:
                    return False
        else:
            return False
