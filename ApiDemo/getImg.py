# -*- coding: utf-8 -*-
# __author__ = Roger
import requests

# import cStringIO, urllib2, Image
# url = 'http://www.jb51.net/images/logo.gif'
# file = urllib2.urlopen(url)
# tmpIm = cStringIO.StringIO(file.read())
# im = Image.open(tmpIm)


def get_image(url):
    response = requests.get(url)
    img_size = int(response.headers['Content-Length']) / 1024.0
    return img_size


if __name__ == '__main__':
    get_image('http://l0.51fanli.net/app/images/2016/12/585b29853260b.jpg')