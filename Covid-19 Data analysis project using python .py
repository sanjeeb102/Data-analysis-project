#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the libraries
import pandas as pd


# In[3]:


#importing the dataset using the URL
df = pd.read_csv("https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv")


# In[4]:


df.head()


# In[6]:


#finding the no. of rows & columns in the dataset
df.shape


# In[7]:


#Data types of columns
df.dtypes


# In[7]:


#info and describe of data in dataframe
df.info


# In[20]:


df.describe


# In[5]:


#unique values in location column.
df['location'].nunique()


# In[6]:


#Maximum frequency using values counts.
df['continent'].value_counts(ascending = False)


# In[7]:


#maximum and mean value in total_cases
df['total_cases'].max()


# In[24]:


df['total_cases'].mean()


# In[36]:


#25%,50%,75% quartile values in 'total_deaths'
df['total_deaths'].quantile([0.25,0.50,0.75])


# In[8]:


#continent having maximum human_development_index
df[['continent','human_development_index']].value_counts(ascending=False).head(1)


# In[9]:


#continent has minimum 'gdp_per_capita'
df[['continent','gdp_per_capita']].value_counts(ascending=True).head(1)


# In[10]:


#Filtering the dataframe
df = df[['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']]
df


# In[11]:


#Data cleaning
df.drop_duplicates()


# In[12]:


#Missing values
df.isnull().sum()


# In[13]:


#removing observation where continent column value is missing
df.dropna(subset = ['continent'])


# In[14]:


#Filling missing values 0
df.fillna(0)


# In[15]:


#convert date column in datetime format using pandas.to_datetime
df['date'] = pd.to_datetime(df['date'])
df.dtypes


# In[16]:


#Create new column month 
df['Month'] = pd.DatetimeIndex(df['date']).month
df.head()


# In[17]:


#Data aggregation
df2 =df.groupby(['continent']).max()
df2


# In[18]:


#Storing the result in a new dataframe named 'df-groupby'
df_groupby = pd.DataFrame(df2)
df_groupby


# In[21]:


#Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'
total_deaths_to_total_cases = (df['total_deaths'] / df['total_cases'])
total_deaths_to_total_cases


# In[22]:


#Data Visualization :
import seaborn as sns


# In[24]:


#Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot.
sns.histplot(df["gdp_per_capita"],kde=False,color="black",bins=10)


# In[25]:


#Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
sns.relplot(x="gdp_per_capita", y="total_cases", data=df)


# In[26]:


#Plot Pairplot on df_groupby dataset.
df_groupby


# In[27]:


sns.pairplot(df_groupby)


# In[28]:


#Plot a bar plot of 'continent' column with 'total_cases' . Tip : using kind='bar' in seaborn catplot
sns.barplot(x="continent", y="total_cases", data=df)


# In[31]:


#Save the df_groupby dataframe in your local drive using pandas.to_csv function .
df_groupby.to_csv('project.csv')


# In[32]:


pd.read_csv("project.csv")


# In[ ]:




