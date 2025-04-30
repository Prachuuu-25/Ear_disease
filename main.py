from matplotlib import image as mpimg
from matplotlib import pyplot as plt

from PIL import Image,ImageFilter
myImage=Image.open("D:\downloads\images.jpg")
myImage.show()
print(myImage.size)
newImage=myImage.resize((167,91))
print(newImage.size)
newImage.show()
rotatedImage=myImage.rotate(145)
rotatedImage.show()
resizedImage=myImage.resize((50,70))
resizedImage.show()
flippedImage=myImage.transpose(Image.FLIP_LEFT_RIGHT)
flippedImage.show()
flippedImage=myImage.transpose(Image.FLIP_TOP_BOTTOM)
flippedImage.show()
croppedImage=myImage.crop\
(
(
90, 100,
500, 120
)
)
croppedImage.show()
greyImage=myImage.convert("L")
greyImage.show()
blurredImage=myImage.filter(ImageFilter.BoxBlur(5))
blurredImage.show()
