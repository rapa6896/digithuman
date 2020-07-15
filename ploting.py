##check

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def getMinIdx(myArray, image, N):
    min = image[myArray[0]][0]
    minIdx = 0
    for i in range(N):
        if min > image[myArray[i]][0]:
            minIdx = i
    return minIdx

def sameColor(a,b):
    return (a[1]==b[1] and a[2]==b[2] and a[3]==b[3])

def reduceImagePalette(imageColors):
    temp=np.zeros([len(imageColors),4])
    j=0
    for i in imageColors:
        temp[j]=[i[0],int(i[1][0]/10)*10,int(i[1][1]/10)*10,int(i[1][2]/10)*10]
        j+=1
    AfterReduce=[]
    for i in range(len(temp)):
        if(temp[i][0]!=0):
            for j in range(i+1,len(temp)):
                if(sameColor(temp[i],temp[j])):
                    temp[i][0]+=temp[j][0]
                    temp[j][0]=0
            AfterReduce.append(temp[i])
    print(len(imageColors))
    print(len(AfterReduce))
    return AfterReduce

myImage = Image.open("D:/pics_for_digi/211.jpg")
w,l=myImage.size
myImageColors=myImage.getcolors(w*l)
reducedImagePalette=reduceImagePalette(myImageColors)
# print(myImageColors)
# print(reducedImagePalette)
# reducedImagePalette = myImage.convert('P', palette=Image.ADAPTIVE, colors=256)
# reduceImage = reducedImagePalette.convert('RGB', palette=Image.ADAPTIVE)
# reduceImageColors = reduceImage.getcolors()
# print(reducedImagePalette.getcolors())
# print(myImage.getsize())
#
N = 30
min = 0
minidx = 0
dominantColors = [0 for col in range(N)]
j = 0
for i in reducedImagePalette:
    if i[0] > reducedImagePalette[dominantColors[minidx]][0]:
        dominantColors[minidx] = j
        minidx = getMinIdx(dominantColors, reducedImagePalette, N)
    j += 1
theta = np.arange(0, 3.14 * 2, (2*3.14) /N, dtype=float)
radii = np.zeros(N)
width = (2*3.14) / N
colors = np.zeros([N, 3])

for i in range(N):
    colors[i][0] = reducedImagePalette[dominantColors[i]][1] / 255
    colors[i][1] = reducedImagePalette[dominantColors[i]][2] / 255
    colors[i][2] = reducedImagePalette[dominantColors[i]][3] / 255
    radii[i] = reducedImagePalette[dominantColors[i]][0]
print(colors)
print(radii)


ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=1)

plt.show()
