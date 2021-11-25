"""
Created on Wed Oct 20 15:05:55 2021

@author: ymugiran 
"""
import sys
from PIL import Image
import  numpy as np


#Taking image path from user 
image_path=input("Enter image path : ")
#opening image
try:
    
  original_image= Image.open(image_path)
  
except:
    print("That file is not exist")
    sys.exit()

#converting original image into np array
image_rgb= np.asarray(original_image,np.float)


#-----------------Solving for H --------------------------------------------------
#empty array that will holds matrix to solve H 
A = np.empty((0,8), int)
B=np.empty((0,1), int)

#Function that will create a matrix eqaution for a pair points
def create_matrix(c,d,a,b):
    bd=b*d
    bc=b*c
    A1=[c,d,1,0,0,0,(-1*a*c),(-1*a*d)]
    A2=[0,0,0,c,d,1,-1*bc, -1*bd]
    B1=[a]
    B2=[b]
    return A1,A2,B1,B2

#points pair one
A1,A2,B1,B2=create_matrix(230,285,0,0)  
B=np.append(B, np.array([B1,B2]), axis=0) 
A=np.append(A, np.array([A1,A2]), axis=0) 

#points pair two
A1,A2,B1,B2=create_matrix(357,284,600,0)  
B=np.append(B, np.array([B1,B2]), axis=0) 
A=np.append(A, np.array([A1,A2]), axis=0) 

#points pair three
A1,A2,B1,B2=create_matrix(145,522,0,800)  
B=np.append(B, np.array([B1,B2]), axis=0) 
A=np.append(A, np.array([A1,A2]), axis=0)

#points pair four
A1,A2,B1,B2=create_matrix(484,520,600,800)  
B=np.append(B, np.array([B1,B2]), axis=0) 
A=np.append(A, np.array([A1,A2]), axis=0)

#solving for h
h=np.dot(np.linalg.inv(A),B)
h=np.append(h, np.array([[1]]), axis=0)

#reshape h to have H
H=np.reshape(h,(3,3))
# H inverse 
H_inv= np.linalg.inv(H)

# -------------------------End of H solving---------------------------------------------

#New black image with 600 X 800 (This can be changed with repect to the dimenation of original image)
new_img=Image.new("RGB", (600,800),(0,0,0))
#new image array
new_image_from_array = np.asarray(new_img,np.float)
#new image dimenstion (rows and columns)
new_width, new_height = new_img.size
og_width, og_height=original_image.size
#new image pixels
new__img_pixels = new_img.load() 
#original  image pixels
og_img_pixels=original_image.load()


for x in range(1,new_width-1):
    for y in range(1,new_height-1):
        hom_vector= np.dot(H_inv,np.array([x,y,1]))
        a=int(np.round(hom_vector[0]/hom_vector[2]))
        b= int(np.round(hom_vector[1]/hom_vector[2]))
        if a < og_width and b < og_height and x< new_width and y< new_height:
          new__img_pixels[x,y]=og_img_pixels[a,b]
       
new_img.save("new_image_result.png", format="png")


  