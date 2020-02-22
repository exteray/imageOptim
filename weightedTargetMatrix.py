#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from IPython.display import display
import numpy as np


# In[2]:


img = Image.open("target.jpg")
dimension = 28
targetImgWidth = 1400
subimgWidth = targetImgWidth / dimension
print(subimgWidth)


# In[19]:


#display(img)


# In[25]:


outputMatrix = [[None]*dimension]*dimension
for x in range(dimension):
    for y in range(dimension):        
# for x in range(2):
#     for y in range(2):
        
        area = (x * subimgWidth, y *subimgWidth, (x +  1) * subimgWidth, (y + 1)* subimgWidth)
        print(area)
        cropped_img = img.crop(area)
#         cropped_img.show()
        display(cropped_img)
        avgGrayVal = np.array(cropped_img).mean()
        print(avgGrayVal)
        outputMatrix[x][y] = avgGrayVal
print(outputMatrix)


# In[5]:


def getAvgValueMatrix():
    outputMatrix = [[None]*dimension]*dimension
    for x in range(dimension):
        for y in range(dimension):        
    # for x in range(2):
    #     for y in range(2):
            
            area = (x * subimgWidth, y *subimgWidth, (x +  1) * subimgWidth, (y + 1)* subimgWidth)
            print(area)
            cropped_img = img.crop(area)
    #         cropped_img.show()
            display(cropped_img)
            avgGrayVal = np.array(cropped_img).mean()
            print(avgGrayVal)
            outputMatrix[x][y] = avgGrayVal
    print(outputMatrix)
    return outputMatrix


# In[4]:


getAvgValueMatrix()


# In[ ]:




