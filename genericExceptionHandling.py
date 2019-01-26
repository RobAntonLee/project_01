# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:32:12 2019

@author: Rob
"""
#dependencies
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#end dependencies

#exception handling
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("some fucking url")
if title == None:
    print("Hey jockey, its not there, you silly fuck")
else:
    print(title)
#end exception handling
