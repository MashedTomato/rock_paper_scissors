###
# Determines users choice
###

# Import block
import pygame
import gamePieces
import random
###


class Choice:
    def __init__(self):
        self.choice = 0
        self.outcome = " "
        self.win_count = 0
        self.loss_count = 0
        self.draw_count = 0

    def game_choice(self, clicked_choice):
        self.choice = clicked_choice

        if self.choice == 1:
            self.ai()
            if self.ai_choice == 1:
                self.outcome = "Draw"
                print(self.outcome)
            elif self.ai_choice == 2:
                self.outcome = "Lose!"
                print(self.outcome)
            elif self.ai_choice == 3:
                self.outcome = "Win!"
                print(self.outcome)
            else:
                self.outcome = "What fuck?"
                print(self.outcome)
        elif self.choice == 2:
            self.ai()
            if self.ai_choice == 1:
                self.outcome = "Win!"
                print(self.outcome)
            elif self.ai_choice == 2:
                self.outcome = "Draw"
                print(self.outcome)
            elif self.ai_choice == 3:
                self.outcome = "Lose!"
                print(self.outcome)
            else:
                self.outcome = "What fuck?"
                print(self.outcome)
        elif self.choice == 3:
            self.ai()
            if self.ai_choice == 1:
                self.outcome = "Lose!"
                print(self.outcome)
            elif self.ai_choice == 2:
                self.outcome = "Win!"
                print(self.outcome)
            elif self.ai_choice == 3:
                self.outcome = "Draw"
                print(self.outcome)
            else:
                self.outcome = "What fuck?"
                print(self.outcome)
        else:
            self.outcome = "What fuck?"
        self.choice = 0
        if self.outcome == "Win!":
            self.win_count += 1
        elif self.outcome == "Lose!":
            self.loss_count += 1
        elif self.outcome == "Draw":
            self.draw_count += 1

    def ai(self):
        self.ai_choice = random.randint(1, 3)

    def draw_choice(self, size, screen):

        game_font = pygame.font.Font(None, 25)
        txt_surface = game_font.render(str(self.outcome), True, (10, 10, 10))
        txt_rect = txt_surface.get_rect(
            topleft=(size * 2 + size / 2, size * 2 + size / 2))

        win_loss_surface = game_font.render(
            f"W: {self.win_count} L: {self.loss_count} D: {self.draw_count}", True, (10, 10, 10))
        win_loss_rect = win_loss_surface.get_rect(
            midtop=(txt_rect.centerx, txt_rect.bottom))

        screen.blit(txt_surface, txt_rect)
        screen.blit(win_loss_surface, win_loss_rect)
