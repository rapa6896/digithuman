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


def plot_polar(t, r, w, c):
    ax = plt.subplot(111, projection='polar')
    ax.bar(t, r, width=w, bottom=0.0, color=c, alpha=1)
    plt.show()
    return


def plot_bar(r, c):
    category_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    labels = ['1']
    data = r

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data).max())

    curr = 0
    for i in range(len(c)):
        widths = data[i]
        starts = curr
        curr += widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=labels, color=c[i])
        xcenters = starts + widths / 2

    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    plt.show()
    return

def printPallet(path, plot): #plot 0 = circle , plot 1 o square visualization
    myimage = None
    try:
        myImage = Image.open(path)
    except:
        return

    reducedImagePalette = myImage.convert('P', palette=Image.ADAPTIVE, colors=256)
    reduceImage = reducedImagePalette.convert('RGB', palette=Image.ADAPTIVE)
    reduceImageColors = reduceImage.getcolors()




    N = 10
    min = 0
    minidx = 0
    dominantColors = [0 for col in range(N)]
    j = 0
    for i in reduceImageColors:
        if i[0] > reduceImageColors[dominantColors[minidx]][0]:
            dominantColors[minidx] = j
            minidx = getMinIdx(dominantColors, reduceImageColors, N)
        j += 1
    theta = np.arange(0, 3.14 * 2, (2 * 3.14) / N, dtype=float)
    radii = np.zeros(N)
    width = (2 * 3.14) / N
    colors = np.zeros([N, 3])

    for i in range(N):
        colors[i][0] = reduceImageColors[dominantColors[i]][1][0] / 255
        colors[i][1] = reduceImageColors[dominantColors[i]][1][1] / 255
        colors[i][2] = reduceImageColors[dominantColors[i]][1][2] / 255
        radii[i] = reduceImageColors[dominantColors[i]][0]
    if(plot==1):
        plot_bar(radii, colors)
    else:
        plot_polar(theta,radii,width,colors)

# #
#
# #
# # def sameColor(a,b):
# #     return (a[1]==b[1] and a[2]==b[2] and a[3]==b[3])
# #
# # def reduceImagePalette(imageColors):
# #     temp=np.zeros([len(imageColors),4])
# #     j=0
# #     for i in imageColors:
# #         temp[j]=[i[0],int(i[1][0]/10)*10,int(i[1][1]/10)*10,int(i[1][2]/10)*10]
# #         j+=1
# #     AfterReduce=[]
# #     for i in range(len(temp)):
# #         if(temp[i][0]!=0):
# #             for j in range(i+1,len(temp)):
# #                 if(sameColor(temp[i],temp[j])):
# #                     temp[i][0]+=temp[j][0]
# #                     temp[j][0]=0
# #             AfterReduce.append(temp[i])
# #     return AfterReduce
