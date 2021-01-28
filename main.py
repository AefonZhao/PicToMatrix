from PIL import Image
import os
import cv2
import numpy as np

def getConcentration(img, d, inputPath, outputPath):
    cen = (int(img.size[0]/ 2), int(img.size[1]/2))
    array = []
    for i in range(cen[0], cen[0] + d):
        for j in range(cen[1], cen[1] + d):
            r, g, b = img.getpixel((i, j))
            rgb = (r, g, b)
            array.append(rgb)
    r_aver, g_aver, b_aver = 0, 0, 0
    for i in range(len(array)):
        r_aver = r_aver + array[i][0]
        g_aver = g_aver + array[i][1]
        b_aver = b_aver + array[i][2]

    r_aver = r_aver / len(array)
    g_aver = g_aver / len(array)
    b_aver = b_aver / len(array)
    c = (int(r_aver), int(g_aver), int(b_aver))
    return c

    fileName=inputPath
    img=Image.open(fileName)
    size=img.size

    weight=(size[0]/300)
    height=(size[1]/400)
    res=np.zeros((300,400))

    for i in range(0, 300):
        for j in range(0, 400):
            box1=(weight * i, height * j, weight * (i + 1), height * (j + 1))
            region=img.crop(box1)
            c1=getConcentration(region, 1)
            # Only for red color
            if (c1[0]-150)>c1[1]:
                res[i][j]=1

    np.savetxt(outputPath, res)
