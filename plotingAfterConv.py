from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def getMinIdx(myArray, image, N):
    min = 1000**3
    minIdx = 0
    for i in range(N):
        if myArray[i]==-1:
            return i
        if min > image[myArray[i]][0]:
            minIdx = i
    return minIdx


def plot_polar(t, r, w, c,pathToSave):
    ax = plt.subplot(111, projection='polar')
    ax.bar(t, r, width=w, bottom=0.0, color=c, alpha=1)

    if(pathToSave!=""):
        plt.savefig(pathToSave,dpi=400)
    plt.show()
    return


def plot_bar(r, c,pathToSave):
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


    if (pathToSave != ""):
        plt.savefig(pathToSave,dpi=400)
    plt.show()
    return

def printPallet(path, plot,colorRange,pathToSave):  # plot 0 = circle , plot 1 o square visualization
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
    minidx = -1
    dominantColors = [-1 for col in range(N)]
    j = 0
    for i in reduceImageColors:
        x=i[1][0]
        y=i[1][1]
        z=i[1][2]
        if x+y+z>=colorRange[0] and x+y+z<colorRange[1]:
            if dominantColors[minidx] == -1:
                dominantColors[minidx] = j
                minidx = getMinIdx(dominantColors, reduceImageColors, N)
            elif i[0] > reduceImageColors[dominantColors[minidx]][0]:
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
    if (plot == 1):
        plot_bar(radii, colors,pathToSave)
    else:
        plot_polar(theta, radii, width, colors,pathToSave)




