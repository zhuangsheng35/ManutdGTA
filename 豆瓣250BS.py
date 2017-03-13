import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


page = urlopen("https://movie.douban.com/top250")
content=page.read().decode("utf-8")
soup = BeautifulSoup(content, "lxml")

#print(soup.find_all("em"))
title=soup.select('span[class="title"]')
other=soup.select('span[class="other"]')
rating_num=soup.select('span[class="rating_num"]')
quote=soup.select('p[class="quote"]')
print(title)
# <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292052/" class="">
#                             <span class="title">肖申克的救赎</span>
#                                     <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
#                                 <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
#                         </a>
#
#
#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
#                             1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
#                         </p>
#
#
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.6</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>797362人评价</span>
#                         </div>
#
#                             <p class="quote">
#                                 <span class="inq">希望让人自由。</span>
#                             </p>
#                     </div>
#                 </div>''''