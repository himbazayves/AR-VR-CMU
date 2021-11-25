"""
Created on Wed Oct 20 15:05:55 2021

@author: ymugiran 
"""
import sys
from PIL import Image
import  numpy as np
import math

#opening an image
original_image= Image.open("g.jpg")
#original image dimension
width, height = original_image.size
#creating a new black image 
new_img=Image.new("RGB", (1024,1024),(0,0,0))
#new image dimension
new_width, new_height = new_img.size

d=width
z=d
N=1024
delta = 180/N

#calculating max phi and teta
max_phi=math.atan(height/(2*d)) * (180/math.pi)
max_teta=math.atan(width/(2*d)) * (180/math.pi)

phi=np.linspace(-90, 90, N)
teta=np.linspace(-90, 90, N)

#loading og image and new image pixels
og_img_pixels=original_image.load()
new__img_pixels = new_img.load() 

for i in  np.linspace(-90,90, N):
   t=i
   for j in  np.linspace(-90,90, N):
        p=j
        if p< max_phi and t< max_teta:
            #calculating r
            r=z/( math.cos(math.radians(p)) * math.cos(math.radians(t)) )
            #calculating x
            x=r*(math.cos(math.radians(p)))*(math.sin(math.radians(t)))
            #calculating y
            y=r*(math.sin(math.radians(p)))
            #CICS to PICS
            pics_x=np.round(x+(height/2))
            pics_y=np.round(y+(width/2))
            
            
            if height>pics_x and width >pics_y  :
                if pics_x>0 and pics_y>0:
                    i=t/delta
                    j=p/delta
                    #pixel value from original image to new image
                    new__img_pixels[j+(new_height/2),i+(new_width/2)]=og_img_pixels[pics_y,pics_x]
new_img.save("result.jpg")


