from asyncwindow import AsyncWindow
from time import time, sleep

window = AsyncWindow(500, 500)
while window.is_running():
    sleep(1)
