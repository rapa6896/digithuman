import json
from PIL import Image
import numpy as np
import math
import os
import combine
import sortedImags
import plotingAfterConv
import grayscale
import priceAndRat


def printArtist(artist,colorRange):
    k = open('ndata.txt', 'r')
    info = json.load(k)
    dir = ""
    imgs=[]
    f=0
    try:
        os.mkdir(artist)
        dir = artist + "/"
    except OSError:
        print ("Creation of the directory %s failed" % dir)
    for data in info['data']:
        if data["artist"] == artist:
            curImg = None
            path = data["image_path"]
            try:
                curImg = Image.open(data["image_path"])
            except:
                continue
            if "'" in data["title"] or "." in data["title"]  or ":" in data["title"] or "-" in data["title"]  :
                title=str(f)
            else:
                title= data["title"]
            nameImg = dir + title + " img.jpg"


            curImg.save(nameImg)
            plotBarName = dir + title + " PlotBar.jpg"
            plotPolName = dir + title + " PlotPol.jpg"
            plotingAfterConv.printPallet(nameImg, 1, colorRange, plotBarName)
            plotingAfterConv.printPallet(nameImg, 0, colorRange, plotPolName)
            imgs.append(curImg)
            f+=1

    totalImgNum = len(imgs)
    imgnum = 0
    x = int(math.sqrt(totalImgNum * 5 / 9))
    y = int(totalImgNum / x)
    paths = []
    for j in range(y):
        to_comb_row = []
        for i in range(x):
            to_comb_row.append(imgs[imgnum])
            imgnum += 1
        curImg = combine.combineImageRow(to_comb_row)
        name = dir + str(imgnum)
        name += ".jpg"
        curImg.save(name)
        paths.append(name)

    imgs = [Image.open(i) for i in paths]
    finle_img = combine.combineImageCol(imgs)
    imgPath = dir + artist + " img.jpg"
    finle_img.save(imgPath)
    plotBarName = dir + artist + " PlotBar.jpg"
    plotPolName = dir + artist + " PlotPol.jpg"
    plotingAfterConv.printPallet(imgPath, 1, colorRange, plotBarName)
    plotingAfterConv.printPallet(imgPath, 0, colorRange, plotPolName)
