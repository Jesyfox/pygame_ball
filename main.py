
import pygame
import os

SCREEN_SIZE = (700, 500)
BALL_SIZE = (100, 100)

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image, image.get_rect()


# Initialise screen
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_area = screen.get_rect()
pygame.display.set_caption('Ball')

# Fill background
background, background_rect = load_png('beach.jpg')
background = pygame.transform.scale(background, SCREEN_SIZE)

# Object
ball_image, ball_rect = load_png('ball.png')
ball_image = pygame.transform.scale(ball_image, (100, 100))
ball_rect.w, ball_rect.h = (100, 100)


def main():

    gravity = 15
    ball_is_jumping = False
    jump_count = 10

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        pygame.time.delay(40)
        event = pygame.key.get_pressed()

        dx, dy = 0, 0
        (x, y) = ball_rect.x, ball_rect.y
        vel = 10

        # STRAFING
        if event[pygame.K_LEFT]:
            if screen_area.x < x:
                dx -= vel
        elif event[pygame.K_RIGHT]:
            if screen_area.w - ball_rect.w >= x:
                dx = vel

        if not ball_is_jumping:
            if event[pygame.K_SPACE]:
                ball_is_jumping = True
        else:
            if jump_count >= 0:
                dy -= (jump_count ** 2) * 0.4
                jump_count -= 1
            else:
                ball_is_jumping = False
                jump_count = 10

        # GRAVITY
        if screen_area.h - ball_rect.h > y and not ball_is_jumping:
            dy += gravity

        ball_rect.x, ball_rect.y = (x + dx, y + dy)

        # screen.blit(background, background_rect)
        screen.blit(ball_image, ball_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
