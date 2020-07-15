import os
import urllib.request as req
import json

c = 0


def get_image_path(imgurl):
    err=0
    path=""
    try:
        path = 'D:/pics_for_digi//'
        path = os.path.join(path, str(c))
        path += ".jpg"
        req.urlretrieve(imgurl, path)
    except:
        err=1


    return path, err


def get_artist_url(a):
    path="www.amazon.com"+a
    return path


k = open('mard_metadata.json', 'r')
line = k.readline()
ndata = {}
ndata['data'] = []
while line != "":
    data = json.loads(line)
    if "price" in data and "artist" in data and "title" in data and "categories" in data and "salesRank" in data and "imUrl" in data and "artist_url" in data and "root-genre" in data and "first-release-year" in data:
        image_path,err=get_image_path(data["imUrl"])
        if (not err):
            ndata['data'].append(
                {
                    "title": data["title"],
                    "artist": data["artist"],
                    "categories": data["categories"],
                    "main_category": data["root-genre"],
                    "release-year": data["first-release-year"],
                    "salesRank": data["salesRank"],
                    "price": data["price"],
                    "image_path": image_path,
                    "artist_url": get_artist_url(data["artist_url"]),

                }
            )
            c += 1
        else:
            print("broken link")
    line = k.readline()


with open('ndata.txt', 'w') as outfile:
    json.dump(ndata, outfile)
