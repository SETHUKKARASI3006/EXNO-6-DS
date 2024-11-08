# -*- coding: utf-8 -*-
"""EX NO6:Data visualization Using Seaborn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A3nhw0cGQhMcJhxLw-OymOlkER_Ul3_S

**Data visualization Using Seaborn**
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Datas
x = [1, 2, 3, 4, 5]
y = [3, 6, 2, 7, 1]

# Create line plot using seaborn

x = [1, 2, 3, 4, 5]
y1 = [3, 5, 2, 6, 1]
y2 = [1, 6, 4, 3, 8]
y3 = [5, 2, 7, 1, 4]

# implement line plot and include all the necessary parameters

plt.figure(figsize=(8,5)) 
sns.lineplot(x=x, y=y) 
plt.title("Line Plot") 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
plt.show()

plt.figure(figsize=(8,5)) 
sns.lineplot(x=x, y=y1, label="y1") 
sns.lineplot(x=x, y=y2, label="y2") 
sns.lineplot(x=x, y=y3, label="y3") 
plt.title("Multiple Line Plot") 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
plt.legend() 
plt.show()

"""**Bar Plot - Seaborn**"""

tips = sns.load_dataset('tips')

# Implement Bar plot with hue parameter
plt.figure(figsize=(8,5)) 
sns.barplot(x='day', y='total_bill', hue='sex', data=tips, palette='viridis')

# Set labels and title
plt.title("Total Bill by Day and Gender") 
plt.xlabel("Day") 
plt.ylabel("Total Bill") 
plt.show()

# Include titanic dataset
tit=pd.read_csv("/content/titanic_dataset.csv")
tit

plt.figure(figsize=(8,5))
# Implement barplot using seaborn and set x='Embarked',y='Fare',data=tit, palette='rainbow' and set graph title as "Fare of Passenger by Embarked Town"
sns.barplot(x='Embarked', y='Fare', data=tit, palette='rainbow') 
plt.title("Fare of Passenger by Embarked Town") 
plt.xlabel("Embarked") 
plt.ylabel("Fare") 
plt.show()

plt.figure(figsize=(8,5))
# Implement barplot using seaborn and set x='Embarked',y='Fare',data=tit, palette='rainbow',hue='Pclass' and set graph title as "Fare of Passenger by Embarked Town, Divided by Class"
sns.barplot(x='Embarked', y='Fare', data=tit, palette='rainbow', hue='Pclass') 
plt.title("Fare of Passenger by Embarked Town, Divided by Class") 
plt.xlabel("Embarked") 
plt.ylabel("Fare") 
plt.show()

import seaborn as sns
# using tips dataset implement Scatter plot of total bill vs tip amount
plt.figure(figsize=(8,5)) 
sns.scatterplot(x='total_bill', y='tip', data="tips")

# Set labels and title
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.title('Scatter Plot of Total Bill vs. Tip Amount')

"""**VIOLIN PLOT**"""

# implement violinplot by comparing any two values from titanic data set
plt.figure(figsize=(8,5)) 
sns.violinplot(x='Pclass', y='Age', data=tit, palette='muted') 
plt.title("Age Distribution by Passenger Class") 
plt.xlabel("Pclass") 
plt.ylabel("Age") 
plt.show()

"""**HISTOGRAM**"""

import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(0)
marks = np.random.normal(loc=70, scale=10, size=100)

# Generating dataset of random numbers
np.random.seed(1)
num_var = np.random.randn(1000)
num_var = pd.Series(num_var, name = "Numerical Variable")
num_var

# IMPLEMENT HISTOGRAM
plt.figure(figsize=(8,5)) 
sns.histplot(num_var, kde=True, bins=30) 
plt.title("Histogram of Numerical Variable") 
plt.xlabel("Value") 
plt.ylabel("Frequency") 
plt.show()

# IMPLEMENT histplot in seaborn and set parameters data=df,x=Pclass,hue=Survived,kde=True
plt.figure(figsize=(8,5)) 
sns.histplot(data=tit, x='Pclass', hue='Survived', kde=True, multiple="stack") 
plt.title("Histogram of Pclass with Survival") 
plt.xlabel("Pclass") 
plt.ylabel("Count") 
plt.show()
