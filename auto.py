from PIL import Image
import autopy
import time

from PIL import Image
import autopy
import time

autopy.mouse.move(500,500)
autopy.mouse.click()
autopy.mouse.click()
time.sleep(3)
#kan = autopy.bitmap.capture_screen()
#autopy.bitmap.Bitmap.save(kan,".jpg")

width, height = 200,200

left = 5
top = height / 4
right = 164
bottom = 3 * height / 4

bitmap_object = autopy.bitmap.capture_screen()
bitmap_object.save('img/path.png')
im = Image.open(r"img/path.png")
  
# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size
  
# Setting the points for cropped image
left = 400
top =  170
right = 1680
bottom = 840 
  
# Cropped image of above dimension
# (It will not change orginal image)
im1 = im.crop((left, top, right, bottom))
im1.save("pathreal.png")
