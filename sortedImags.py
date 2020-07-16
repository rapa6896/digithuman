import json
from PIL import Image
import numpy as np
import math
import os
import combine


def sortKey(elem):
    return elem[0]


def getSortedImage_with_years(artist, genre, all, years):
    geners = ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
    k = open('ndata.txt', 'r')
    info = json.load(k)
    imgs = []
    for data in info['data']:
        if (artist != "" and artist == data["artist"]) or (genre != "" and data["main_category"] == genre) or (
                all and data["main_category"] != "" and data["main_category"] in str(geners)):
            if data["release-year"] != "":
                year = int(data["release-year"])
                if ((year >= years[0]) and (year < years[1])):
                    curImg = None
                    path = data["image_path"]
                    try:
                        curImg = Image.open(data["image_path"])
                    except:
                        continue
                    imgs.append([year, data["image_path"], curImg])

    imgs.sort(key=sortKey)
    return imgs


def getSortedImage(artist, genre, all, years):
    geners = ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
    k = open('ndata.txt', 'r')
    info = json.load(k)
    imgs = []
    for data in info['data']:
        if (artist != "" and artist == data["artist"]) or (genre != "" and data["main_category"] == genre) or (
                all and data["main_category"] != "" and data["main_category"] in str(geners)):
            if data["release-year"] != "":
                year = int(data["release-year"])
                if ((year >= years[0]) and (year < years[1])):
                    curImg = None
                    path = data["image_path"]
                    try:
                        curImg = Image.open(data["image_path"])
                    except:
                        continue
                    imgs.append([year, curImg])

    imgs.sort(key=sortKey)
    return [row[1] for row in imgs]


def CombineImageFromArray(imgs, name_to_save):
    totalImgNum = len(imgs)
    imgnum = 0
    x = int(math.sqrt(totalImgNum * 5 / 9))
    y = int(totalImgNum / x)
    paths = []

    dir = name_to_save + "/"
    try:
        os.mkdir(name_to_save)
    except OSError:
        print ("Creation of the directory %s failed" % name_to_save)
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


def sortAndCombineImage(artist, genre, All, years, finale_file_name):
    sortedImgs = getSortedImage(artist, genre, All, years)
    finale = CombineImageFromArray(sortedImgs, finale_file_name)
    return finale
