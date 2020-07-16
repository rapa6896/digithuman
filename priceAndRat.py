import json
from PIL import Image
import numpy as np
import math
import os
import combine


def combineImagePriceOrRank(interPrice, interRank, name_to_save):
    geners = ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
    k = open('ndata.txt', 'r')
    info = json.load(k)
    imgs = []
    for data in info['data']:
        Rank = int((data["salesRank"])["Music"])
        price = (data["price"])
        if ((interPrice and (price >= interPrice[0]) and (price < interPrice[1])) or (
                interRank and (Rank >= interRank[0]) and (Rank < interRank[1]))) and (
                data["main_category"] != "" and data["main_category"] in str(geners)):
                curImg = None
                path = data["image_path"]
                try:
                    curImg = Image.open(data["image_path"])
                except:
                    continue
                imgs.append(curImg)

    totalImgNum = len(imgs)
    imgnum = 0
    x = int(math.sqrt(totalImgNum * 5 / 9))
    y = int(totalImgNum / x)
    paths = []

    dir = name_to_save + "/"
    try:
        os.mkdir(name_to_save)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        dir = ""
    for j in range(y):
        to_comb_row = []
        for i in range(x):
            to_comb_row.append(imgs[imgnum])
            imgnum += 1
        curImg = combine.combineImageRow(to_comb_row)
        name = dir + str(imgnum) + name_to_save
        name += ".jpg"
        curImg.save(name)
        paths.append(name)

    imgs = [Image.open(i) for i in paths]
    finle_img = combine.combineImageCol(imgs)
    finle_img.show()
    finle_img.save(name_to_save + ".jpg")

    return finle_img
