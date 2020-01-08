from tkinter import Tk, Canvas
from PIL import Image, ImageTk

root = Tk()
canv = Canvas(root, width = 800, height = 600, background = "gray")
canv.pack()

img = Image.open("testImage.png")
imgTk = ImageTk.PhotoImage(img)

canv.create_image(imgTk.width()/2, imgTk.height()/2, image = imgTk)
canv.update()

root.mainloop()