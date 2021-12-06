import sys
from PIL import Image
import  numpy as np
import math
from skimage.measure import block_reduce


image = Image.open("C:/Users/Ronald Tumuhairwe/Desktop/CMU/FIRST -YEAR/Fall/AVR/labs/lab-3/Rwanda_SRTM30meters(2).tif")
img = np.array(image)
max=img.max()
min=img.min()

img[img  == max] = 0
new_max=img.max()
print(f"min is {min} , max is {max}, new max { new_max}")

img=img*(new_max/255)
image_max=block_reduce(img, block_size=(10, 10), func=np.max)
#image_max=image_max*round((new_max/255))

#image_max=image_max*15
min_2=image_max.min()
new_min=min_2

# img=Image.fromarray(image_max.astype(np.uint8))


# width, height = img.size

def linearizing(min, max,new_min, new_max,value):
    return (((value-min)* (new_max-new_min)) / (max-min)+new_min)

image_max=linearizing(new_min,new_max,-1000,180,image_max)
T=linearizing(new_min,new_max,-1000,180,2000)
min_2=linearizing(new_min,new_max,-1000,180,min)
print(f"Threshold {T}")
# print(image_max.shape)
img=Image.fromarray(image_max.astype(np.uint8))
width, height = img.size
image_pix=img.load()
# file = open('./part-2/results/Rwanda.obj', 'a')
file = open('C:/Users/Ronald Tumuhairwe/Desktop/CMU/FIRST -YEAR/Fall/AVR/labs/lab-3/part-2/Rwanda-test.obj', 'a')

file.write(f"mtllib master_custom.mtl")
file.write("\n")
current_color=""
# T=2700
colors_list=["Yellow"]
count=0
for x in range(1,width-1):
   
    for y in range(1,height-1):
        my_list=[]
        # my_list= np.array(my_list)
        color=""
        if  x< width and y< height:
                   
                    v1=image_pix[x,y]
                    my_list.append(int(v1))
                    v2=image_pix[x,y+1]
                    my_list.append(int(v2))
                    v3=image_pix[x+1,y]
                    my_list.append(int(v3))
                    my_list= np.array(my_list)
                    max_v=my_list.min() 
                    
                    if max_v<min_2:
                        current_color="usemtl green"
                        
                    elif max_v>T:
                        current_color="usemtl blue"  

                    else :
                        current_color="usemtl red"
                    
                    file.write(f"{current_color}")
                    file.write("\n")
                    file.write(f"v   {x} {y} {image_pix[x,y]}")
                    file.write("\n")  
                    file.write(f"v   {x} {y+1}  {image_pix[x,y+1]}")
                    file.write("\n")  
                    file.write(f"v   {x+1} {y}  {image_pix[x+1,y]}")
                    file.write("\n") 
                    file.write(f"f -3 -2 -1")
                    file.write("\n")  

                    my_list=[]
                    v1=image_pix[x+1,y]
                    my_list.append(int(v1))
                    v2=image_pix[x,y+1]
                    my_list.append(int(v2))
                    v3=image_pix[x+1,y+1]
                    my_list.append(int(v3))
                    my_list= np.array(my_list)
                    max_v=my_list.min() 
                    
                    if max_v<min_2:
                        current_color="usemtl green"
                        
                    elif max_v>T:
                        current_color="usemtl blue"  

                    else :
                        current_color="usemtl red" 


                    file.write(f"{current_color}")
                    file.write("\n")
                    file.write(f"v   {x+1} {y} {image_pix[x+1,y]}")
                    file.write("\n")  
                    file.write(f"v   {x} {y+1}  {image_pix[x,y+1]}")
                    file.write("\n")  
                    file.write(f"v   {x+1} {y+1}  {image_pix[x+1,y+1]}")
                    file.write("\n")  
                    file.write(f"f -3 -2 -1")
                    file.write("\n")    
                    
                    
                    
                    
                    
                    
                    
                   