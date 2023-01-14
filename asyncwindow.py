from time import time, sleep, strftime
from threading import Thread
import os


class AsyncWindow:
    window = None
    width, height = 0, 0
    last_keys = None

    def is_running(self):
        return self.pygame_thread.isAlive()

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.pygame_thread = Thread(target=self.pygame_thread_main)
        self.pygame_thread.run()

    def pygame_thread_main(self):
        import pygame

        pygame.init()
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Labyrinth")
        self.last_keys = pygame.key.get_pressed()
        run = True

        while run:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            if keys[pygame.K_ESCAPE] or (keys[pygame.K_LALT] and keys[pygame.K_F4]):
                run = False
                pass
            self.last_keys = keys

        raise SystemExit()

