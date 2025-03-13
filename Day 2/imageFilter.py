# Name: Dia Yamamoto
# Purpose: This program filters and changes the colors of the images

import matplotlib.pyplot as plt

#input/output images
inpic = "Zucker_NH.png"
outpic = "Zucker.png"

# middle man 
img = plt.imread(inpic) #load image
#plt.imshow(img) # show user image
#plt.show() # show image
img2 = img.copy() # create copy

# turn off red and green colors
img2[:,:,0] = 0   # turn off red colors 
img2[:,:,1] = 0   # turn off green colors

# Let's test out what we've learned! 
# what happens when you change the ':' of the RGB to other numbers..?
# if you are not sure, modify your code and see what happens when you run it!

#show image to user and program
plt.imshow(img2) # show user image
plt.show() # show image

# save new image to file
plt.imsave(outpic, img2)
