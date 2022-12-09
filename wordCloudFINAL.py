#Importing Libraries
#Start with loading all necessary libraries
import numpy as np
import pandas as pd

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
#matplotlib inline

stopwords = set(STOPWORDS)
stopwords.update(["voter","will", "voter", "s", "t", "let", "don"])


df = pd.read_csv("testerCleaned.csv", index_col=0)

text = df.at[1,'x']

for col in range(1, df.size):
    text += df.at[col, 'x']


# Create and generate a word cloud image:
#wordcloud = WordCloud(stopwords=stopwords, background_color="white"()).generate(text)
wordcloud = WordCloud( width=480, height=600, margin=0, stopwords=stopwords, background_color="white", scale = 20).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
#plt.show()
plt.savefig("wordCloudTest.svg")
