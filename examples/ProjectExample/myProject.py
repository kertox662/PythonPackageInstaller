from pipinstaller import install
install()

from PIL import Image
img = Image.open("testImage.png")
img.show()