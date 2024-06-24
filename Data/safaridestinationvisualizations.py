# -*- coding: utf-8 -*-

import os
from os import path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import pyarrow

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
file_path = path.join(d, 'Tanzania_Safari2.csv')

df = pd.read_csv(file_path, encoding="utf-8")

df.dropna(inplace=True)

#df['Price'] = df['Price'].replace('[^\d.]', '', regex=True).astype(float)

df['Price'] = df['Price'].replace('[^\d.]', '', regex=True).astype(float)


sortd = df.sort_values(by='Price', ascending=False)

cmap = plt.cm.get_cmap('YlOrBr')

plt.figure(figsize=(20, 8))
bars = plt.barh(sortd['Company'], sortd['Price'], color=cmap(sortd['Price']/sortd['Price'].max()))
plt.xlabel('Price in USD')
plt.title('Safari Companies Ranked by Prices', fontsize=30)

sm = plt.cm.ScalarMappable(cmap=cmap)
sm.set_array(sortd['Price'])

plt.show()
plt.savefig('Safari Companies Ranked by Prices.png')


df['Price Group'] = pd.qcut(df['Price'], q=3, labels=('Cheap', 'Affordable', 'Expensive'))

plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(x='Price', y='Duration (days)', size='Duration (days)', hue='Price Group', sizes=(50, 200), palette='viridis', data=df)
plt.title('Which is the Best Deal for You', fontsize=30)
plt.xlabel('Price')
plt.ylabel('Duration (days)')

legend = plt.legend(title='Price Group')
legend.get_title().set_fontsize('12')

plt.show()
plt.savefig('Which is the Best Deal for You.png')
