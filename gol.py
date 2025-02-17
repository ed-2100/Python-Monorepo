import numpy as np
import pygame, sys

pygame.init()

fpsClock = pygame.time.Clock()

WIDTH = 200
HEIGHT = 200
pps = 5
'''pixels per square'''

window_surface = pygame.display.set_mode((WIDTH * pps, HEIGHT * pps))
screen_array = pygame.surfarray.pixels2d(window_surface)

pygame.display.set_caption("GOL")

past_state = np.full((WIDTH, HEIGHT), False)
current_state = past_state.copy()

def draw_helper():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            screen_array[row * pps : row * pps + pps, col * pps : col * pps + pps] = 0x00 if past_state[row, col] else 0xFFFFFF

def update_state():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            sx = col - 1 if col != 0 else 0
            ex = col + 2 if col < WIDTH else WIDTH
            sy = row - 1 if row != 0 else 0
            ey = row + 2 if row < HEIGHT else HEIGHT
            sum = np.sum(past_state[sy:ey, sx:ex]) - past_state[row, col]
            current_state[row, col] = sum == 3 or sum == 2 and past_state[row, col]

pygame.display.set_caption("GOL")

draw_helper()

inPlay = False
count = 0
while True:
    if inPlay:
        update_state()
        current_state, past_state = past_state, current_state
        draw_helper()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                inPlay = True
            elif event.key == pygame.K_LSHIFT:
                inPlay = False
            elif event.key == pygame.K_r:
                past_state[:] = np.random.randint(0, 2, size=past_state.shape) != 0
                draw_helper()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==pygame.BUTTON_LEFT:
                past_state[event.pos[0] // pps, event.pos[1] // pps] = True
                draw_helper()
            elif event.button==pygame.BUTTON_RIGHT:
                past_state[event.pos[0] // pps, event.pos[1] // pps] = False
                draw_helper()

    pygame.display.update()

    if count % 10 == 0:
        print(fpsClock.get_fps())
    count += 1

    fpsClock.tick(0 if inPlay else 60)
