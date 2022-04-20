from main import main, display_image
from PIL import Image


image = Image.open('test.png')
main(image, 0.5)
