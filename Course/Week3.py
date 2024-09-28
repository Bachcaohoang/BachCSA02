import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SNOWBOARDER_SIZE = 10
ROCK_SIZE = 50
SPEED = 5

# Load the rock image
rock_image = pygame.image.load('Course/rock.png')
rock_image = pygame.transform.scale(rock_image, (ROCK_SIZE, ROCK_SIZE))

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Snowboarder:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH / 2, HEIGHT / 2, SNOWBOARDER_SIZE, SNOWBOARDER_SIZE)
        self.speed = SPEED

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

class Rock:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ROCK_SIZE), random.randint(0, HEIGHT - ROCK_SIZE), ROCK_SIZE, ROCK_SIZE)
        self.speed = SPEED

    def draw(self):
        screen.blit(rock_image, self.rect)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = WIDTH
            self.rect.y = random.randint(0, HEIGHT - ROCK_SIZE)

class Game:
    def __init__(self):
        self.snowboarder = Snowboarder()
        self.rocks = [Rock() for _ in range(10)]
        self.start_time = time.time()
        self.score = 0
        self.paused = False

    def draw(self):
        screen.fill((255, 255, 255))  # White background to represent snow
        self.snowboarder.draw()
        for rock in self.rocks:
            rock.draw()

        if time.time() - self.start_time < 5:
            font = pygame.font.Font(None, 100)
            text = font.render(str(int(5 - (time.time() - self.start_time))), True, (0, 0, 0))
            screen.blit(text, (WIDTH / 2 - 20, HEIGHT / 2 - 50))
        else:
            font = pygame.font.Font(None, 30)
            text = font.render("Score: " + str(self.score), True, (0, 0, 0))
            screen.blit(text, (10, 10))

        if self.paused:
            font = pygame.font.Font(None, 100)
            text = font.render("Paused", True, (0, 0, 0))
            screen.blit(text, (WIDTH / 2 - 50, HEIGHT / 2 - 50))

    def update(self):
        if not self.paused:
            if time.time() - self.start_time >= 5:
                self.snowboarder.update()
                for rock in self.rocks:
                    rock.update()
                    if self.snowboarder.rect.colliderect(rock.rect):
                        print("Game Over. Your score was " + str(self.score))
                        pygame.quit()
                        sys.exit()
                    if rock.rect.x < self.snowboarder.rect.x:
                        self.score += 1
                        rock.rect.x = WIDTH
                        rock.rect.y = random.randint(0, HEIGHT - ROCK_SIZE)

def main():
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.paused = not game.paused
                if event.key == pygame.K_o and game.paused:
                    game.paused = False

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()