# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:57:48 2021

@author: Ymugiran
"""

import sys
from PIL import Image
import  numpy as np
import math
import pandas as pd
import csv
from scipy import signal

from scipy import misc

file=pd.read_csv("star_data_lots.csv")
#removing can and proper columns
file=file.drop(['con', 'proper'], axis = 1)
#convert ra to longitude
file['ra']=file['ra']*15
file=file[1:]
rounded_mag=[] 

imageArray=np.zeros((1081,900), np.uint8)

#Round all intensities larger than 5.00 down to 5.00  and put them in rounded_mag list
for i in range(1,len(file)+1) :
    mag=file.loc[i, "mag"]
    if mag >5:
        rounded_mag.append(5) 
    else:
        rounded_mag.append(mag) 
file['mag']=rounded_mag


file['dec']=(-1)*(file['dec'])


# function that scale mag
def scale(n):
   
    s=((n)*(-36.491))+202.45
    return s


#function that interpolate long to heights
def long_to_pix(long):
    y=((long)*(3))+0
    return y

#function that interpolate laltitude to width
def lat_to_pix_to_pix(lat):
    y=((lat)*(4.44))+400
    return y

#scaling mag to intensity
intensity=[]
for index, row in file.iterrows():
    mag=scale(row['mag'])
    intensity.append(mag)
file['intensity']=intensity


#interpolating creating image
for  index, row in file.iterrows():
    long=row['ra']
    lat=row['dec']
    imageArray[round(long_to_pix(long)), round(lat_to_pix_to_pix(lat))]=round(row['intensity'])
    
    #print(imageArray[round(long_to_pix(long)), round(lat_to_pix_to_pix(lat))])
 
#convolve image    
convK=np.asarray(  [ (0.0,0.5,0.0),(0.5,1.0,0.5), (0.0,0.5,0.0) ] , np.float32)    
imageArray=signal.convolve2d(imageArray,convK, 'same', 'fill', fillvalue=0)

#save image
Image.fromarray(imageArray.astype(np.uint8)).save("result.jpg")


