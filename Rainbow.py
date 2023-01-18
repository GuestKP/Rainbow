from asyncwindow import *
from time import time, sleep
import serial
from serial.tools import list_ports
import pygame
from random import randint


def draw_window(surface: pygame.Surface, width: int, height: int) -> None:
    global arr, i
    #arr[i] = randint(0, 499)
    i = i + 1 if i != LENGTH-1 else 0
    # example code for this function
    surface.fill((255, 255, 255))
    pygame.draw.lines(surface, (255, 0, 0), False, [[idx, height - val - 1] for idx, val in enumerate(arr)])


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


LENGTH = 500
arr = [0] * LENGTH
i = 0
# print([[i.description, i.device] for i in list_ports.comports()])
slave = serial.Serial('COM11', 9600)
# slave.write('asd'.ncode())

window = AsyncWindow(500, 500, draw_window, event_callback, keys_checker)
# window.run()

while True:
    # arr[i] = int.from_bytes(slave.read(4), 'little')
    arr[i] = randint(0, 500)
    if i == LENGTH - 1:
        arr = [0] * LENGTH
        i = 0
    else:
        i += 1
    print(arr)
    sleep(0.01)  # serial read and other things

# here should be serial.close()
