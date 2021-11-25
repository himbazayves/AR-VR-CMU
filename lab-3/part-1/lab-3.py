# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:28:49 2021

@author: ymugiran
"""

import sys
from PIL import Image
import  numpy as np
import math
from skimage.measure import block_reduce




#open image
image = Image.open("./files/Rwanda_SRTM30meters(2).tif")
#transforma image into an array 
img = np.asarray(image,np.uint16)
#find image max eleavation
max=img.max()
#find image min elevation
min=img.min()
#elevation  outside Rwanda to b e0
img[img  == max] = 0
#find new max
new_max=img.max()

print(f"min is {min} , max is {max}, new max { new_max}")
#scale latitude
image_max=img*round((new_max/255))
#image_max=image_max*15
min_2=image_max.min()

Image.fromarray(image_max.astype(np.uint8)).save("./part-1/results/final_part1-result.jpeg")


