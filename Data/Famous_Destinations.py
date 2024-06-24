# -*- coding: utf-8 -*-

import os
from os import path
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import openpyxl

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
file_path = path.join(d, 'Tanzania_Safari2.csv')

data = pd.read_csv(file_path, encoding="utf-8")

text = str(data['Description'])

stopwords = set(STOPWORDS)
stopwords.add("Days")
stopwords.add("Day")
stopwords.add("Big")
stopwords.add("Tanzania")
stopwords.add("Safari")
stopwords.add("Name")
stopwords.add("Object")
stopwords.add("Pl")
stopwords.add("Five")
stopwords.add("Ma")
stopwords.add("S")
stopwords.add("dtype")
stopwords.add("Ap")

wordcloud = WordCloud(
    background_color="orange",
    stopwords=stopwords,
    width=800,
    height=660,
    margin=1
).generate(text)

plt.figure(figsize=(20, 18))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Famous Safari Destinations", fontsize=50)
plt.show()

plt.savefig("Famous Safari Destinations.png")
data.to_excel('Tanzania_Safari.xlsx')
