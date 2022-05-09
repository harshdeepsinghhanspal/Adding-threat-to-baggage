#Not so mandatory step but can be done at your own wish
from PIL import Image, ImageEnhance

#read the image
im = Image.open("Mix/step-2.png")

#image contrast enhancer
enhancer = ImageEnhance.Contrast(im)

factor = 3.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('Mix/result.png')