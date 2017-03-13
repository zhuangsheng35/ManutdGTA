# -*- coding: utf-8 -*-
import urllib.request
import json
from city import city

cityname = input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
   url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
   content =urllib.request.urlopen(url).read()
   data=json.loads(content)
   result=data['weatherinfo']
   srt_temp=('%s\n%s~%s')%(
      result['weather'],
      result['temp1'],
      result['temp2']
      )
   print(srt_temp)
