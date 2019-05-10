#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


data = pd.read_csv('C:\\Users\\HP Spectre\\testData\\crime.csv');


# In[10]:


data.columns
data.shape


# In[11]:


data.dropna()


# In[12]:


data.tail(5)


# In[13]:


data = data[pd.notnull(data['NEIGHBOURHOOD'])]


# In[26]:


data.tail(5)
#data is clean here


# In[31]:


print (data['YEAR'])


# In[14]:


year = data['YEAR']


# In[15]:


year.describe()


# In[26]:


timeFrame = year.unique()
len(timeFrame)
timeFrame
#there are in total 17 years


# In[17]:


data.describe()


# In[18]:


type = data['TYPE']
print(type.unique())
#no violent crimes are included in this data set


# In[ ]:


occurence = []

for x in timeFrame:
    count = 0
    for i in year:
        if int(x) == int(i):
        	count+=1
        year.drop(i)
    occurence.append(count)


# In[ ]:


y_pos = np.arange(len(timeFrame))#all the unique years


plt.bar(timeFrame,occurence)
plt.ylabel('Number of Crimes', fontsize = 14)
plt.title('Count of Crime',fontsize=24)
plt.xlabel('Year',fontsize=14)

plt.show()


# In[ ]:





# In[ ]:




