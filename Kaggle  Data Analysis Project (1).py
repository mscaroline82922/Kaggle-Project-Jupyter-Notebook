#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install opendatasets')


# In[2]:


import opendatasets as od


# # Download the dataset from Kaggle open dataset 

# In[3]:


dataset = "https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries"


# In[4]:


od.download(dataset)


# In[5]:


import os


# In[10]:


data_filename = './data-science-job-salaries/ds_salaries.csv' 


# In[7]:


os.listdir(data_dir)


# # Data preparation and cleaning
# 
# #Load the file using pandas
# #Look at some information the file contains, about the data and the columns 
# #Fix any missing or incorrect values
# 
# 

# In[8]:


import pandas as pd


# In[56]:


df = pd.read_csv(data_filename)


# In[57]:


df


# In[58]:


df.columns


# In[ ]:


df=df.drop(labels="Unnamed: 0,", axis=1) 
print(df)


# In[64]:


len(df.columns)


# In[65]:


#view dataframe
df


# # Exploratory Data Analysis 
# 
# #Analyze data types in the dataframe
# #classify data types into numerical and categorical columns
# 
# 

# In[67]:


# check the structure of the datasets
display(df.describe())
display(df.head(10))
display(df.tail(10))
display(df.dtypes.value_counts())


# In[68]:


# Separate categorical variable and numerical variable columns in the dataframe using dtypes function and equality operator
df.dtypes == "object"


# In[69]:


# Separate Numerical variables and categorical variables
num_vars = df.columns[df.dtypes != "object"]
cat_vars = df.columns[df.dtypes =="object"]
print(num_vars)
print(cat_vars)


# In[70]:


#view all numerical variables
df[num_vars]


# In[71]:


# Find misssing values in the numerical variables
df[num_vars].isnull()


# In[72]:


# Find misssing values in the numerical variables
df[num_vars].isnull().sum()


# In[73]:


#view all categorical variables
df[cat_vars]


# In[74]:


# Find misssing values in the categorical variables
df[cat_vars].isnull()


# In[76]:


# Find misssing values in the categorical variables
df[cat_vars].isnull().sum()


# In[77]:


df.describe()


# In[78]:


# Explore the types of datascience jobs available 
df.job_title


# In[79]:


# unique data science jobs in the dataset
df.job_title.unique()


# In[80]:


# number of data science professional job categories in the dataset
data_science_jobs=df.job_title.unique()
len(data_science_jobs)


# In[87]:


#find the average salary by job title in us dollars
salary_by_job_title=(df.groupby('job_title').agg({'salary_in_usd':'mean'}))
salary_by_job_title


# In[89]:


# Find top 20 top earners in USD
salary_by_job_title[:20]


# In[94]:


# Find the top 10 salaries by data science jobs 
salary_by_job_title[:10].plot(kind='barh')


# # Analysis and visualization 
# 
# Ask and answer questions
# 
# #Average salary of datascience professionals by experience level?
# #How about earning of data professionals by company size?
# #Among the top earners by job title, where are the companies located?
# #How many datascience professionals worked 100% remotely between 2020-2022

# In[95]:


import seaborn as sns
sns.set_style("darkgrid")


# In[100]:


# Find the distribution of salary by job title
sns.distplot(salary_by_job_title)


# In[101]:


#find the average salary by experience level,group salary earners by experience and display salary as line chart 
salary_by_experience_level=(df.groupby('experience_level').agg({'salary_in_usd':'mean'}))
salary_by_experience_level


# In[102]:


salary_by_experience_level[:10].plot(kind='line')

