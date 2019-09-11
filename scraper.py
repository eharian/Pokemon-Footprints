from urllib.request import Request, urlopen, FancyURLopener, urlretrieve
from bs4 import BeautifulSoup
import re


class AppURLopener(FancyURLopener):
    version = "Mozilla/5.0"


def getURL(link):
    openURL = AppURLopener()
    response = openURL.open(link)
    bs = BeautifulSoup(response, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.png')})
    res = images[0]['src']
    res = "https:" + res

    return(res)


def downloadImage(link):
    name = re.sub('File:', '', link.split('/')[len(link.split('/'))-1])
    openURL = AppURLopener()
    openURL.retrieve(link, 'Footprints/{}'.format(name))


def main():
    for i in range(1, 810):
        id = "{:03d}".format(i)
        link = 'https://archives.bulbagarden.net/wiki/File:F{}.png'.format(id)
        footprintURL = getURL(link)
        downloadImage(footprintURL)
        print("Downloaded Footprint for Pokemon #{}".format(id))

if __name__ == '__main__':
    main()

