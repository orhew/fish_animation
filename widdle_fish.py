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
    for i in range(10):
        fishes.append(Fish((width/2, height/2)))
    while True:
        clock.tick(60)
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()
            if event.type == py.KEYDOWN:
                if event.type == py.K_d:
                    for i in range(len(fishes) // 2):
                        fishes.pop(0)
        screen.fill(color)
        for fish in fishes:
            fish.update()
        for fish in fishes:
            fish.draw(screen)
        py.display.flip()


if __name__ == '__main__':
    main()