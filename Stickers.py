#!/usr/bin/env python
# coding: utf-8

# In[39]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import os


# In[40]:



path = input("Enter the path of the picture : (enter cwd for current working directory)")

if path == "cwd":
    path = os.getcwd()

while not os.path.isdir(path):
    print("Invalid Path Entered... ")
    path = input("Enter the valid path of the picture : ")
    
name = input("Enter the name of the picture with the extension : ")
os.chdir(path)

while not os.path.isfile(name):
    print("Picture Doesn't Exists!")
    name = input("Enter the valid name of the picture with the extension : ")
    
    
cwd = os.getcwd()


# In[41]:


src = cv2.imread(name)


img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

# plt.imshow(img)
# plt.show()
#cv2.imshow('image', img)

face_detect = cv2.CascadeClassifier("C:\\Users\lenovo\Desktop\mlworkshop\haarcascade_frontalface_alt.xml")
faces = face_detect.detectMultiScale(img, 1.1, 2)

if type(faces) == type(np.array([1])):
    faces = faces.tolist()


# In[42]:


cut = []

if "Stickers" not in os.listdir():
    os.mkdir("Stickers")
os.chdir(cwd + "\\Stickers")

for face in faces:
    
    x, y, h, w = face
    
    today = str(date.today()).replace("-","")
    filename = "STK-" + today + "-WA" + "0"*(4 - len(str(faces.index(face)))) + str(faces.index(face)) + ".webp"#
#    print(filename)
    
    cut.append(img[y : y + h, x : x + w, : ])
    im = cut[-1].copy()
    
    im2save = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
#     im.copy()
    
#     plt.axis("off")
#     plt.imshow(im)
    
#     plt.show()

    _ = cv2.imwrite(filename, im2save)
    
os.chdir(cwd)

