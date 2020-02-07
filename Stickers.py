#!/usr/bin/env python
# coding: utf-8

#imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import os

#Intializing instance of class CascadeClassifier
face_detect = cv2.CascadeClassifier(os.getcwd() + "\\haarcascade_frontalface_alt.xml")

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

src = cv2.imread(name)

#OpenCV uses BGR color format
img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#Location of haarcascade_frontalface_alt.xml file in my PC
faces = face_detect.detectMultiScale(img, 1.1, 2)

#if there are no faces detected, then line 38 return a tuple instead of an array
if type(faces) == type(np.array([1])):
    #To access List functionalities
    faces = faces.tolist()

cut = []

if "Stickers" not in os.listdir():
    os.mkdir("Stickers")
os.chdir(cwd + "\\Stickers")

for face in faces:
    
    x, y, h, w = face
    
    #Making the filename
    today = str(date.today()).replace("-","")
    filename = "STK-" + today + "-WA" + "0"*(4 - len(str(faces.index(face)))) + str(faces.index(face)) + ".webp"
    
    cut.append(img[y : y + h, x : x + w, : ])
    im = cut[-1].copy()
    
    im2save = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    _ = cv2.imwrite(filename, im2save)

#Back to working Directory    
os.chdir(cwd)

