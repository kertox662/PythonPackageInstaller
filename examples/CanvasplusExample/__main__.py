"""Shameless plug, advertisment for CanvasPlus, https://pypi.org/project/canvasplus/, https://github.com/Luke-zhang-04/CanvasPlus/wiki"""
"""
Copyright 2020 Misha Melnyk, Luke Zhang | MIT License
"""
from pipinstaller import install

install(auto=True)

from CanvasPlus import CanvasPlus
from tkinter import Tk
from time import sleep
import asyncio
import math

root = Tk()
screen = CanvasPlus(root, width=1000, height=1000, bg="black")
screen.pack()

arrow = screen.create_arrow(500, 500, 50, 100, 300, 50, fill="grey")

for i in range(360 // 2):
    screen.rotate(arrow, 500, 500, 4, unit="d")
    screen.update()
    sleep(0.01)

screen.delete(arrow)

rect1 = screen.create_polygon(300, 300, 300, 500, 500, 500, 500, 300, fill="blue")
rect2 = screen.clone(rect1)
rect3 = screen.clone(rect1)
rect4 = screen.clone(rect1)


async def _test():
    await asyncio.gather(
        screen.async_rotate(rect1, 300, 300, 1, 2 * math.pi, unit="r", fps=24),
        screen.async_rotate(rect2, 500, 500, 1, 2 * math.pi, unit="rad", fps=24),
        screen.async_rotate(rect3, 300, 500, 1, 360, unit="d", fps=24),
        screen.async_rotate(rect4, 500, 300, 1, 360, unit="deg", fps=24),
    )
    await asyncio.gather(
        screen.async_rotate(rect1, 200, 200, 0.25, 0.5 * math.pi, unit="r", fps=24),
        screen.async_rotate(rect2, 600, 600, 0.25, 0.5 * math.pi, unit="rad", fps=24),
        screen.async_rotate(rect3, 200, 600, 0.25, 90, unit="d", fps=24),
        screen.async_rotate(rect4, 600, 200, 0.25, 90, unit="deg", fps=24),
    )
    await asyncio.gather(
        screen.async_rotate(rect1, 200, 200, 0.25, -0.5 * math.pi, unit="r", fps=24),
        screen.async_rotate(rect2, 600, 600, 0.25, -0.5 * math.pi, unit="rad", fps=24),
        screen.async_rotate(rect3, 200, 600, 0.25, -90, unit="d", fps=24),
        screen.async_rotate(rect4, 600, 200, 0.25, -90, unit="deg", fps=24),
    )


asyncio.run(_test())

screen.update()
screen.mainloop()

print("For more examples, visit https://github.com/Luke-zhang-04/CanvasPlus/wiki")
