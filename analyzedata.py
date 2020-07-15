import json
from PIL import Image
import numpy as np
from plotingAfterConv import *

def getMinIdx(dominantColorsIdx, matrix, N):
    i = dominantColorsIdx[0][0]
    j = dominantColorsIdx[0][1]
    k = dominantColorsIdx[0][2]
    min = matrix[i][j][k]
    minIdx = 0
    for y in range(N):
        i = dominantColorsIdx[y][0]
        j = dominantColorsIdx[y][1]
        k = dominantColorsIdx[y][2]
        if(i==-1):
            minIdx = y
            break
        if min > matrix[i][j][k]:
            minIdx = y
    return minIdx


def new_ganre(geners, genre):
    j = 0
    for i in geners:
        if i[0] == genre:
            return j
        j += 1
    return -1


def printGaners():
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b00 = []
    b10 = []
    k = open('ndata.txt', 'r')
    info = json.load(k)
    for data in info['data']:
        if (data['release-year'] != ''):
            year = int(data['release-year'])
            if (year >= 1960):
                if (year < 1970):
                    b = b6
                elif (year < 1980):
                    b = b7
                elif (year < 1990):
                    b = b8
                elif (year < 2000):
                    b = b9
                elif (year < 2010):
                    b = b00
                else:
                    b = b10
                indexInArray = new_ganre(b, data["main_category"])
                if (indexInArray == -1):
                    b.append([data["main_category"], 1])
                b[indexInArray][1] += 1

    print(b6)
    print(b7)
    print(b8)
    print(b9)
    print(b00)
    print(b10)


# def getDominantColors(genre, ImageColors,N):
#     min = 0
#     minidx = 0
#     dominantColors = [0 for col in range(N)]
#     j = 0
#     for i in ImageColors:
#         if i[0] > ImageColors[dominantColors[minidx]][0]:
#             dominantColors[minidx] = j
#             minidx = getMinIdx(dominantColors, ImageColors, N)
#         j += 1
#     return dominantColors


def getDominantColorsFromMatrix(matrix, N):
    min = 0
    minidx = 0
    dominantColorsIdx = [[-1 for row in range(3)] for col in range(N)]
    min = 0
    j = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            for k in range(matrix.shape[0]):
                matrix[i][j][k]=matrix[i][j][k]*1000
                if matrix[i][j][k] > min:
                    dominantColorsIdx[minidx] = [i, j, k]
                    minidx = getMinIdx(dominantColorsIdx, matrix,N)
                    coord=dominantColorsIdx[minidx]
                    if coord[0]==-1:
                        min==0
                    else:
                        min=matrix[coord[0]][coord[1]][coord[2]]
    colors=np.zeros([N,3])
    ammunt= np.zeros(N)
    for r in range(N):
        i = dominantColorsIdx[r][0]
        j = dominantColorsIdx[r][1]
        k = dominantColorsIdx[r][2]
        ammunt[r]=matrix[i][j][k]
        colors[r]=[(i*10)/255,(j*10)/255,(k*10)/255]



    return ammunt,colors


def add_image_colors(path, colorMatrix):
    myImage = None
    try:
        myImage = Image.open(path)
    except:
        return
    reducedImagePalette = myImage.convert('P', palette=Image.ADAPTIVE, colors=256)
    reduceImage = reducedImagePalette.convert('RGB', palette=Image.ADAPTIVE)
    reduceImageColors = reduceImage.getcolors()
    l, w = reduceImage.size
    for i in reduceImageColors:
        colorMatrix[int(i[1][0] / 10)][int(i[1][1] / 10)][int(i[1][2] / 10)] += i[0] / (l * w)  ## אחוז


def imageColorsByGenre(genre):
    geners = ['rock', 'pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
    colorMatrix = np.zeros([26, 26, 26])
    all = False
    if (genre == ''):
        all = True
    k = open('ndata.txt', 'r')
    info = json.load(k)
    h=0
    for data in info['data']:
        # if h > 50:
        #     break
        curGenre = data["main_category"]
        if(curGenre!="Alternative Rock"):
            all=False
        if all:
            if curGenre != "" and curGenre in str(geners):
                add_image_colors(data["image_path"], colorMatrix)
        else:
            if curGenre==genre:
                add_image_colors(data["image_path"], colorMatrix)
                h += 1

    return colorMatrix


def imageColorsByArtisi(artist):
    colorMatrix = np.zeros([26, 26, 26])
    k = open('ndata.txt', 'r')
    info = json.load(k)
    h = 0
    for data in info['data']:
        # if h > 50:
        #     break
        curArtist = data["artist"]
        if curArtist == artist:
            add_image_colors(data["image_path"], colorMatrix)
            h += 1
    return colorMatrix


# imageColors('rock')
# printGaners()
N=20
# mat=imageColorsByGenre("Pop")
mat=imageColorsByArtisi("Green Day")
r,c=getDominantColorsFromMatrix(mat,N)
theta = np.arange(0, 3.14 * 2, (2 * 3.14) / N, dtype=float)
width = (2 * 3.14) / N
plot_bar(r, c)
# plot_polar(theta,r,width,c)


