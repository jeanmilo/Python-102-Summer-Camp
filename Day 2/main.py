# Set some RGB Colors into a variable!
DarkBLUE = (216, 0 , 50)
LightBLUE = (226, 64, 102)
RED =  (236, 128, 153)
YELLOW = (255, 255, 255)

# Set up the drawing window using a library
from PIL import Image

img = Image.open("Zucker_NH.png") # load our image into img 
img.show() # show img

print([img.getdata])

# create a copy of the image we saved in img
img2 = img.load()
print(img.size)

#create list of pixels 
pixels = img.getdata()
pixel_list = list(pixels)
pixel_list2 = [] # new list for new colors

for pixel in pixel_list: 
  # add values of rgb colors together to determine intensity
  r = pixel[0]
  g = pixel[1]
  b = pixel[2]
  total = r + g + b

  # sort colors by intensity based on total given
  if total < 182: 
    pixel_list2.append(DarkBLUE)
  elif total > 546:
    pixel_list2.append(YELLOW)
  elif total >= 182 and total <= 364:
    pixel_list2.append(RED)
  elif total > 364 and total <= 546: 
    pixel_list2.append(LightBLUE)


newimg = Image.new("RGB", img.size)
newimg.putdata(pixel_list2)
newimg.save("zucker.png", "png")
img = Image.open("zucker.png")
img.show()    












