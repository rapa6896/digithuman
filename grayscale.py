import sortedImags
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

def get_grey_scale_imgs(artist, genre, all,years):
    imgs=sortedImags.getSortedImage_with_years(artist, genre, all,years)
    imgs_and_avr_brightness=[([calculate_brightness(i[2]),i[0],i[2]])for i in imgs]
    return imgs_and_avr_brightness

def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale


def getImage(img):
    return OffsetImage(np.asarray(img.resize([8,8])))


def plotgrayscale(imgs_and_avr_brightness):
    imgs = [(i[2])for i in imgs_and_avr_brightness]
    x = [(i[1])for i in imgs_and_avr_brightness]
    y = [(i[0])for i in imgs_and_avr_brightness]

    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for x0, y0, img in zip(x, y, imgs):
        ab = AnnotationBbox(getImage(img), (x0, y0), frameon=False)
        ax.add_artist(ab)

    plt.show()


def dowhatwineed(artist, genre, all,years):
    grey_scale_imgs=get_grey_scale_imgs(artist, genre, all,years)
    plotgrayscale(grey_scale_imgs)