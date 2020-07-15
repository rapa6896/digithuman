import json
from PIL import Image
import numpy as np
import math
import os


def combineImage(artist, genre, all, years, name_to_save):
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
        curImg = combineImageRow(to_comb_row)
        name = dir + str(imgnum) + name_to_save
        name += ".jpg"
        curImg.save(name)
        paths.append(name)

    imgs = [Image.open(i) for i in paths]
    finle_img = combineImageCol(imgs)
    finle_img.show()
    finle_img.save(name_to_save + ".jpg")

    return finle_img


def combineImageRow(imgs):
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    h=[]
    g=0
    for i in imgs:
        d=np.asarray(i.resize(min_shape))
        try:
            lenz=len(d[0][0])
            succ=g
        except:
            d=np.asarray(imgs[succ].resize(min_shape))
        h.append(d)
        g+=1
    imgs_comb = np.hstack(h)

    # save that beautiful picture
    imgs_comb = Image.fromarray(imgs_comb)
    return imgs_comb


def combineImageCol(imgs):
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    # for a vertical stacking it is simple: use vstack
    imgs_comb = np.vstack((np.asarray(i.resize(min_shape)) for i in imgs))
    imgs_comb = Image.fromarray(imgs_comb)
    return imgs_comb


combineImage("", "", True, [1960, 2016], "ALL")
# ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
