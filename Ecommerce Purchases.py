#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r'Ecommerce Purchases')
data


# # 1. Display top 10 rows of the dataset

# In[3]:


data.head(10)


# # 2. Check last 10 rows of the dataset

# In[4]:


data.tail(10)


# # 3. Check datatype of each column

# In[5]:


data.dtypes


# # 4. Check null values in the dataset

# In[6]:


data.isnull().sum()


# # 5. How many rows and columns are there in our dataset

# In[7]:


len(data.columns)


# In[8]:


len(data)


# In[9]:


data.info()


# # 6. Highest and lowest purchase prices

# In[10]:


data.columns


# In[11]:


data['Purchase Price'].max()


# In[12]:


data['Purchase Price'].min()


# # 7. Average purchase price

# In[13]:


data['Purchase Price'].mean()


# # 8. How many people have French 'fr' as their language?

# In[14]:


data.columns


# In[15]:


data[data['Language'] == 'fr']


# In[16]:


len(data[data['Language'] == 'fr'])


# In[17]:


data[data['Language'] == 'fr'].count()


# # 9. Job title contains Engineer

# In[18]:


data.columns


# In[19]:


data['Job'].str.contains('engineer')


# In[20]:


len(data[data['Job'].str.contains('engineer',case=False)])


# # 10. Find email of the person with the following ip address: 132.207.160.22

# In[21]:


data.columns


# In[22]:


data[data['IP Address'] == "132.207.160.22"]['Email']


# # 11. How many people have mastercard as their credit card provider and made a purchase above 50?

# In[23]:


data.columns


# In[24]:


len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price'] > 50)])


# # 12. Find the email of the person with the following credit card number: 4664825258997302

# In[25]:


data.columns


# In[26]:


data[data['Credit Card'] == 4664825258997302]['Email']


# # 13. How many people purchase during AM and How many people purchase during PM?

# In[27]:


data.columns


# In[28]:


data['AM or PM'].value_counts()


# # 14. How many people have a credit card that expires in 2020?

# In[29]:


data.columns


# In[30]:


data['CC Exp Date']


# In[31]:


def fun():
    count = 0
    for date in data['CC Exp Date']:
        if date.split('/')[1]=='20':
            count=count+1
    print(count)


# In[32]:


fun()


# #### so, 988 people's credit card will expire in 2020

# In[33]:


data.columns


# In[34]:


len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')])


# # 15. Top 5 most popular email providers

# In[35]:


list1 = []
for email in data['Email']:
    list1.append(email.split('@')[1])


# In[36]:


data['temp'] = list1


# In[37]:


data.head(1)


# In[38]:


data['temp'].value_counts().head()

