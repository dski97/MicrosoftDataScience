#get the url of the page to scrape
url = "https://en.wikipedia.org/wiki/Georg_Wilhelm_Friedrich_Hegel"

#import the requests library
import requests
text = requests.get(url).content.decode('utf-8')

#convert the html to plain text
from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    script = False
    res = ""
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ["script", "style"]:
            self.script = True
    def handle_endtag(self, tag):
        if tag.lower() in ["script", "style"]:
            self.script = False
    def handle_data(self, data):
        if str.strip(data)=="" or self.script:
            return
        self.res += ' ' + data.replace('[  edit  ]', '')


parser = myHTMLParser()
parser.feed(text)
text = parser.res

#get insights from the text
import sys
import nlp_rake

extractor = nlp_rake.Rake(max_words=2,min_freq=3,min_chars=5)
res = extractor.apply(text)

#visualize the data with matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud

wc = WordCloud(background_color="white", width=800, height=600)
plt.figure(figsize=(15,7))
plt.imshow(wc.generate(text))
wc.generate(text).to_file("wordcloud.png")