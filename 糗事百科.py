# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

user_agent ="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"
page = urlopen("http://www.qiushibaike.com/hot/page/")
content=page.read().decode("utf-8")
soup = BeautifulSoup(content, "lxml")

print(soup)