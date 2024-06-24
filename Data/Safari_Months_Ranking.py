# -*- coding: utf-8 -*-

import os
from os import path
import pandas as pd
import openpyxl

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
file_path = path.join(d, 'Best_Safari_Month.csv')

df = pd.read_csv(file_path, encoding="utf-8")

df['Months'] = df['Month'].str.split('-').str[0]
df['Ranking'] = df['Month'].str.split('-').str[1]
df = df.drop(columns='Month')
df = df[['Months', 'Ranking', 'Details']]

df.to_excel('Best_Safari_Month_Clean.xlsx')
