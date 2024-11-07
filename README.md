# EXNO-6-DS-DATA VISUALIZATION USING SEABORN LIBRARY
<br>

# Aim:
<br>
  To Perform Data Visualization using seaborn python library for the given datas.
<br>

# EXPLANATION:
<br>
Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.
<br>

# Algorithm:
<br>
STEP 1:Include the necessary Library.
<br>

STEP 2:Read the given Data.
<br>

STEP 3:Apply data visualization techniques to identify the patterns of the data.
<br>

STEP 4:Apply the various data visualization tools wherever necessary.
<br>

STEP 5:Include Necessary parameters in each functions.
<br>

# Coding and Output:
<br>
```
Developed By: SETHUKKARASI C
Register Number: 212223230201
```
<br>

```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("titanic_dataset.csv")
df.head()
```
<br>

![o1](/1.png)
<br>

```
x=[1,2,3,4,5]
y=[3,6,2,7,1]
sns.lineplot(x=x,y=y)
plt.title('Line Plot')
```
<br>

![o2](/2.png)
<br>

```
x=[1,2,3,4,5]
y1=[3,5,2,6,1]
y2=[1,6,4,3,8]
y3=[5,2,7,1,4]
sns.lineplot(x=x,y=y1,label="line 1")
sns.lineplot(x=x,y=y2,label="line 2")
sns.lineplot(x=x,y=y3,label="line 3")
plt.legend()
plt.title('Multi Line Plot')
```
<br>

![o3](/3.png)
<br>

```
plt.figure(figsize=(8,5))
sns.barplot(x='Embarked',y='Fare',data=df,palette='rainbow')
plt.title("Fare Of Passenger By Embarked Town")
```
<br>

![o4](/4.png)
<br>

```
plt.figure(figsize=(8,5))
sns.barplot(x='Embarked',y='Fare',data=df,palette='rainbow',hue="Pclass")
plt.title("Fare Of Passenger By Embarked Town, Divided by Class")
```
<br>

![o5](/5.png)
<br>

```
sns.scatterplot(x="Age", y="Fare", data=df)
plt.title('Scatterplot of Age vs Fare')
plt.show()
```
<br>

![o6](/6.png)
<br>

```
sns.scatterplot(x="Age", y="Fare", size="Pclass", data=df, sizes=(30, 200))
plt.title('Bubble Chart of Age vs Fare, Size by Passenger Class')
plt.show()
```
<br>

![o7](/7.png)
<br>

```
sns.histplot(data=df,x="Pclass",hue="Survived",kde=True)
```
<br>

![o8](/8.png)
<br>

```
sns.boxplot(x='Pclass',y='Age',data=df,palette='rainbow')
plt.title("Age By Passenger Class")
```
<br>

![o9](/9.png)
<br>

```
sns.violinplot(x="Pclass", y="Fare", data=df, palette='rainbow')
plt.title('Violin Plot of Fare by Passenger Class')
plt.show()
```
<br>

![o10](/10.png)
<br>

```
sns.kdeplot(data=df['Age'], shade=True)
plt.title('Density Plot of Passenger Ages')
plt.show()
```
<br>

![o11](/11.png)
<br>

```
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Titanic Dataset')
plt.show()
```
<br>

![o12](/12.png)
<br>

# Result:
<br>
 Data visualization is successfully performed using seaborn library for the given data.
