import combine
import sortedImags
import plotingAfterConv
import grayscale
import priceAndRat

# ['Rock', 'Pop', 'Classical', 'Jazz', 'Latin Music', 'Metal']


# ___________________combine img witיout sorting
# ___________________combine.combineImage(artist, genre, All, years, finale file name)
# ___________________only one!!!!!:
# ___________________artist: string of the artist name or ""
# ___________________genre: string of the artist name or ""
# ___________________All: True\False
# ___________________years: [int:a,int:b] only album thet a<= release-year < b
# ___________________finale file name: string

# combine.combineImage("", "Jazz", False, [1960, 2016], "Jazz")
plotingAfterConv.printPallet("Jazz.jpg", 1,[150,256])
# ___________________combine img sorted by year
# ___________________combine.combineImage(artist, genre, All, years, finale file name)
# ___________________ only one!!!!!:
# ___________________ artist: string of the artist name or ""
# ___________________ genre: string of the artist name or ""
# ___________________ All: True\False
# ___________________ years: [int:a,int:b] only album thet a<= release-year < b
# ___________________finale file name: string

# sortedImags.sortAndCombineImage("", "Latin Music", False, [1960, 2016], "Latin Music")
#


# ___________________combineImagePriceOrRank(priceR, rankR, finale file name)
# ___________________priceR: None OR [int(low),int(high)]
# ___________________rankR:None OR [int(low),int(high)]
# ___________________finale file name: string

# numberOfIntevals = 3
# jampRank = 1000
# jampPrice = 5
# colorRange=[0,256*3]
# for i in range(numberOfIntevals):
#     minRank = i * jampRank
#     maxRank = (i + 1) * jampRank
#     nameRank = "renk_" + str(minRank) + "_" + str(maxRank)
#     minPrice = i * jampPrice
#     maxPrice = (i + 1) * jampPrice
#     namePrice = "Price_" + str(minRank) + "_" + str(maxRank)
#     try:
#         priceAndRat.combineImagePriceOrRank(None, [minRank, maxRank], nameRank)
#         priceAndRat.combineImagePriceOrRank([minPrice, maxPrice], None, namePrice)
#         plotingAfterConv.printPallet(namePrice + ".jpg", 1,colorRange)
#     except:
#         continue
#
#
#
# _____________________dowhatwineed(artist, genre, all,years):
# grayscale.dowhatwineed("", "", True, [1960, 2016])
