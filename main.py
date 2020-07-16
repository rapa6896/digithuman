import combine
import sortedImags
import plotingAfterConv
import grayscale

# ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
def sortKey(elem):
    return elem[0]


# combine img witיout sorting
# combine.combineImage(artist, genre, All, years, finale file name)
# only one!!!!!:
# artist: string of the artist name or ""
# genre: string of the artist name or ""
# All: True\False
# years: [int:a,int:b] only album thet a<= release-year < b
# finale file name: string

# combine.combineImage("", "Metal", False, [1960, 2016], "Metal")

# combine img sorted by year
# combine.combineImage(artist, genre, All, years, finale file name)
# only one!!!!!:
# artist: string of the artist name or ""
# genre: string of the artist name or ""
# All: True\False
# years: [int:a,int:b] only album thet a<= release-year < b
# finale file name: string

# sortedImags.sortAndCombineImage("", "Latin Music", False, [1960, 2016], "Latin Music")
# plotingAfterConv.printPallet("Jazz.jpg", 1)

# g = grayscale.get_grey_scale_imgs("", "Metal", False, [1960, 2016])


grayscale.dowhatwineed("", "", True, [1960, 2016])