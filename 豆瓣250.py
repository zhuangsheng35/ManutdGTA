# -*- coding: utf-8 -*-
import urllib.request
import re

for id in range(0,251,25):

    url= 'http://movie.douban.com/top250?start=' + str(id)
    con=urllib.request.urlopen(url).read().decode("utf-8")
    number=re.findall('<em class="">(.*?)</em>',con)
    title=re.findall('<span class="title">(.[^&]*?)</span>',con)
    other=re.findall('<span class="other">(.*?)</span>',con)

    
    star=re.findall('<span class="rating_num" property="v:average">(.*?)</span>',con)
    commit=re.findall('<span>(.*?)</span>',con)
    inq=re.findall('<span class="inq">(.*?)</span>',con)
    
    result=zip(number,title,other,commit,star,inq)
    for i in result:
        print(i)
