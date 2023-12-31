# -*- coding: utf-8 -*-
"""Analise medicamentos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u49CzynbTP3o6SokZBy_cjDbM9kOamgX
"""

#importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#upload do arquivo
from google.colab import files
arq = files.upload()

df = pd.read_excel('medicamentos.xlsx')

import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a DataFrame
df = pd.read_excel('medicamentos.xlsx')

# Extract the columns of interest
df = df[['Data', 'Descrição Material']]

# Convert the 'Data' column to datetime and extract the year
df['Year'] = pd.to_datetime(df['Data']).dt.year

# Group the data by year and product and count the number of occurrences
counts = df.groupby(['Year', 'Descrição Material']).size().reset_index(name='Count')

# Plot the data as a bar chart with separate bars for each year
years = counts['Year'].unique()
products = counts['Descrição Material'].unique()
num_products = len(products)
fig, ax = plt.subplots()
for i, year in enumerate(years):
    data = counts[counts['Year'] == year]
    x = range(i, i + num_products)
    ax.bar(x, data['Count'], label=year)
ax.set_xticks(range(num_products//2, (num_products * len(years)), num_products))
ax.set_xticklabels(products)
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.title('Quantity of Medications per Year')
plt.legend()

# Show the plot
plt.show()