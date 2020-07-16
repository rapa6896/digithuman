import combine
import sortedImags
import plotingAfterConv
import grayscale
import priceAndRat

# ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']
#
#
# # combine img witיout sorting
# # combine.combineImage(artist, genre, All, years, finale file name)
# # only one!!!!!:
# # artist: string of the artist name or ""
# # genre: string of the artist name or ""
# # All: True\False
# # years: [int:a,int:b] only album thet a<= release-year < b
# # finale file name: string
#
# combine.combineImage("", "Metal", False, [1960, 2016], "Metal")
#
# # combine img sorted by year
# # combine.combineImage(artist, genre, All, years, finale file name)
# # only one!!!!!:
# # artist: string of the artist name or ""
# # genre: string of the artist name or ""
# # All: True\False
# # years: [int:a,int:b] only album thet a<= release-year < b
# # finale file name: string
#
# sortedImags.sortAndCombineImage("", "Latin Music", False, [1960, 2016], "Latin Music")
# plotingAfterConv.printPallet("Jazz.jpg", 1)
#
#
#
#combineImagePriceOrRank(priceR, rankR, finale file name)
#priceR: None OR [int(low),int(high)]
#rankR:None OR [int(low),int(high)]
#finale file name: string
priceAndRat.combineImagePriceOrRank(None, [2000,3000], "renk_2000_3000")
plotingAfterConv.printPallet("price_0_10.jpg", 1)
#
#
#
#
# grayscale.dowhatwineed("", "", True, [1960, 2016])