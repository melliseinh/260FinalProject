#Importing Libraries
#Start with loading all necessary libraries
import numpy as np
import pandas as pd

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
stopwords.update(["voter","will", "https", "now", "bit.ly", "bit", "ly", "u", "gt", "voter", "s", "t", "let", "don"])


#Load in CSV, change based on which dataset being anlyzed currently
df = pd.read_csv("middlePolitical10Percent.csv")

messages = df["message"]

text = ""

print(messages.size)

for index, value in messages.items():
    if(type(value) == str):
       text += value


# Create and generate a word cloud image:

wordcloud = WordCloud(margin=0, stopwords=stopwords, background_color="white", scale = 20).generate(text)
 
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
#plt.show()

#Set file name for word cloud
plt.savefig("wordCloudMiddlePolitical.svg")
