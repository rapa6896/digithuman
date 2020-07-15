import json
from PIL import Image
import numpy as np
import math


def combineImage(artist, genre, all, years, name_to_save):
    geners = ['rock', 'pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
    k = open('ndata.txt', 'r')
    info = json.load(k)
    imgs = []
    for data in info['data']:
        if (artist != "" and artist == data["artist"]) or (genre != "" and data["main_category"] == genre) or (
                all and data["main_category"] != "" and data["main_category"] in str(geners)):

            if data["release-year"]!="" :
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

    for j in range(y):
        to_comb_row = []
        for i in range(x):
            to_comb_row.append(imgs[imgnum])
            imgnum += 1
        curImg = combineImageRow(to_comb_row)
        name = str(imgnum) + name_to_save
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
    imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))

    # save that beautiful picture
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save('jjjjjj.jpg')
    return imgs_comb


def combineImageCol(imgs):
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))

    # for a vertical stacking it is simple: use vstack
    imgs_comb = np.vstack((np.asarray(i.resize(min_shape)) for i in imgs))
    imgs_comb = Image.fromarray(imgs_comb)
    return imgs_comb


combineImage("", "Rock", False,[1970, 1980], "s")
