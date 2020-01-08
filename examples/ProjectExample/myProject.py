from lib.install_packages import install
install()

from PIL import Image
img = Image.open("testImage.png")
img.show()