import combine
import sortedImags
import plotingAfterConv


# ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
def sortKey(elem):
    return elem[0]

# combine img witיout sorting
# combine.combineImage(artist, genre, All, year, finale file name)
# only one!!!!!:
# artist: string of the artist name or ""
# genre: string of the artist name or ""
# All: True\False
# year: [int:a,int:b] only album thet a<= release-year < b
# finale file name: string
combine.combineImage("", "Metal", False, [1960, 2016], "Metal")



# combine img sorted by year
# combine.combineImage(artist, genre, All, year, finale file name)
# only one!!!!!:
# artist: string of the artist name or ""
# genre: string of the artist name or ""
# All: True\False
# year: [int:a,int:b] only album thet a<= release-year < b
# finale file name: string
sortedImags.sortAndCombineImage("", "Metal", False, [1960, 2016], "MetalSorted")
# plotingAfterConv.printPallet("Jazz.jpg", 1)


