# bounce.py
#
# Exercise 1.5

# ratio = 3 / 5 
# height = 100.0
# for x in range(10):
#     height = height * ratio
#     print(x + 1, round(height, 4))

import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall(
    './/pt'
):
    print(pt.text)
