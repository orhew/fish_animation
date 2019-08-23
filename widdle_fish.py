import sys
from fish import Fish
import pygame as py
import random

py.init()
screen_info = py.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = py.display.set_mode(size)
clock = py.time.Clock()

color = (0, 127, 255)
fishes = []


def main():
    global screen
    for i in range(10):
        fishes.append(Fish((width/2, height/2)))
    while True:
        clock.tick(60)
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()
            if event.type == py.MOUSEBUTTONDOWN:
                fishes.append(Fish(event.pos))
            if event.type == py.KEYDOWN:
                if event.key == py.K_d:
                    sprites = fishes.sprites()
                    for i in range(len(fishes) // 2):
                        sprites[i].kill()
                elif event.key == py.K_f:
                    screen = py.display.set_mode(size, py.FULLSCREEN)
                elif event.key == py.K_ESCAPE:
                    screen = py.display.set_mode(size)
        screen.fill(color)
        for fish in fishes:
            fish.update()
            fish.draw(screen)
        py.display.flip()


if __name__ == '__main__':
    main()
