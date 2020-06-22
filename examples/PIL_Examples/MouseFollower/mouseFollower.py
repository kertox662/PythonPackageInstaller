from tkinter import Tk, Canvas
from PIL import Image, ImageTk
from math import atan2, degrees

root = Tk()
canv = Canvas(root, width=800, height=600, background="white")
canv.pack()
canv.update()
w = canv.winfo_width()
h = canv.winfo_height()

mouseCoords = [w, h / 2]
arrowObj = 0
angle = 0

img = Image.open("arrow.png")
imgTk = ImageTk.PhotoImage(img)


def updateAngle(x, y):
    global angle
    dy = (
        y - h / 2
    )  # considers the origin to be the middle of the screen and not (0,0) by offsetting
    dx = x - w / 2
    angle = atan2(dy, dx)  # atan2 takes in coords and returns an angle


def drawArrow():
    global imgTk, arrowObj
    imgTk = ImageTk.PhotoImage(
        img.rotate(degrees(-angle))
    )  # Have to do -angle. img.rotate() probably rotates clockwise.
    if arrowObj == 0:
        arrowObj = canv.create_image(w / 2, h / 2, image=imgTk)
    else:
        canv.itemconfig(arrowObj, image=imgTk)
        #   Note: By using itemconfig, you can skip two steps:
        #   1. Deleting objects
        #   2. Updating Canvas
        #   (actually updating canvas from event causes recursion
        #   for some reason and causes the program to crash eventually)


def handleMouseEvent(event):
    updateAngle(event.x, event.y)
    drawArrow()


root.bind(
    "<Motion>", handleMouseEvent
)  # Whenever the mouse moves, handleMouseEvent is called

root.mainloop()
