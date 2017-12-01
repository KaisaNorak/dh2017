import urllib.request
from wordcloud import WordCloud
pilv=WordCloud().generate(open("aisakell").read())
pilt=pilv.to_image()
pilt.save('pilt4.png')