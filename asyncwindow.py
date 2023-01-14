from threading import Thread
import os
import pygame
from typing import Callable, Any

KEY_FREE = 0
KEY_RELEASED = 1
KEY_PRESSED = 2
KEY_HOLD = 3


class AsyncWindow:
    surface = None
    last_keys = None
    event_callback = None

    def is_running(self) -> bool:
        return self.pygame_thread.isAlive()

    def __init__(self, width: int, height: int, draw_window: Callable[[pygame.Surface, int, int], Any],
                 event_callback: Callable[[pygame.event.Event], bool], keys_update: Callable[[list[int]], bool],
                 is_resizable: bool = False) -> None:
        """
        Main constructor for AsyncWindow. To run defined window, call AsyncWindow.run().
        :param width: default width of window in pixels
        :param height: default height of window in pixels
        :param draw_window: external function for drawing on window
        :param event_callback: external function for event handling.
                    Should return *True* if window must continue execution; *False* otherwise
        :param keys_update: external function for keys state checking.
                    Should return *True* if window must continue execution; *False* otherwise
        :param is_resizable: flag: can user resize window
        """
        self.pygame_thread = Thread(target=self.pygame_thread_main,
                                    args=[width, height, is_resizable])
        self.event_callback = event_callback
        self.keys_update = keys_update
        self.draw_window = draw_window

    def run(self) -> None:
        """
        Runs window with options defined by constructor of this class.
        """
        self.pygame_thread.run()

    def pygame_thread_main(self, width, height, is_resizable) -> None:
        """
        Main function for window thread. Executes callbacks, checks event and other things related to window.\n
        Should **NOT** be called manually.
        """
        import pygame

        self.init_vars(width, height, is_resizable)

        while True:
            if self.manage_events():
                break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LALT] and keys[pygame.K_F4]:
                break
            if not self.keys_update([int(keys[i]) * 2 + int(self.last_keys[i]) for i in range(512)]):
                break
            self.last_keys = keys

            self.draw_window(self.surface, self.surface.get_width(), self.surface.get_height())
            pygame.display.update()
            pygame.display.flip()

        exit()  # closes thread

    def init_vars(self, width: int, height: int, is_resizable: bool) -> None:
        """
        Initializes window and internal vars.\n
        Should **NOT** be called manually.
        """

        pygame.init()
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        self.surface = pygame.display.set_mode((width, height), pygame.RESIZABLE if is_resizable else 0)
        pygame.display.set_caption("Labyrinth")
        self.last_keys = pygame.key.get_pressed()

    def manage_events(self) -> bool:
        """
        Manages events get from pygame window.
        :return: **True** if window should stop execution and close; **False** otherwise.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.VIDEORESIZE:
                self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            else:
                if not self.event_callback(event):
                    return True
        return False
