from asyncwindow import *
from time import time, sleep
import pygame


def draw_window(surface: pygame.Surface, width: int, height: int) -> None:
    # example code for this function
    surface.fill((255, 255, 255))


def event_callback(event: pygame.event.Event) -> bool:
    # example code for this function
    if event.type == pygame.MOUSEBUTTONDOWN:
        print('Mouse button', event.button, 'pressed at', event.pos, f'({event})')

    return True  # should return True for execution to continue


def keys_checker(keys: list[int]) -> bool:
    # example code for this function
    if keys[pygame.K_SPACE] == KEY_PRESSED:
        print("Space pressed")
    if keys[pygame.K_SPACE] == KEY_HOLD:
        pass  # do nothing while space is *held*
    if keys[pygame.K_SPACE] == KEY_RELEASED:
        print("Space released")

    return True  # should return True for execution to continue


window = AsyncWindow(500, 500, draw_window, event_callback, keys_checker)
window.run()
while window.is_running():
    sleep(1)  # serial read and other things

# here should be serial.close()
