import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess Animal Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 40)

# Questions
questions = [
    ("Big animal with trunk", "elephant", "🐘"),
    ("Says meow", "cat", "🐱"),
    ("King of jungle", "lion", "🦁"),
    ("Yellow fruit", "banana", "🍌"),
]

random.shuffle(questions)

current = 0
score = 0
user_text = ""
feedback = ""

clock = pygame.time.Clock()

running = True

while running:

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:

                answer = questions[current][1]

                if user_text.lower() == answer:
                    feedback = "Correct!"
                    score += 1
                else:
                    feedback = "Wrong!"

                current += 1
                user_text = ""

                if current >= len(questions):
                    running = False

            else:
                user_text += event.unicode

    if current < len(questions):

        clue = questions[current][0]
        emoji = questions[current][2]

        # Clue
        clue_text = font.render(clue, True, BLACK)
        screen.blit(clue_text, (100, 100))

        # Emoji
        emoji_font = pygame.font.SysFont("Segoe UI Emoji", 120)
        emoji_surface = emoji_font.render(emoji, True, BLACK)
        screen.blit(emoji_surface, (300, 200))

        # Input box
        pygame.draw.rect(screen, BLACK, (200, 450, 400, 50), 2)

        input_surface = font.render(user_text, True, BLACK)
        screen.blit(input_surface, (220, 460))

        # Feedback
        feedback_surface = font.render(feedback, True, GREEN)
        screen.blit(feedback_surface, (300, 530))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

print("Final Score:", score)
sys.exit()
