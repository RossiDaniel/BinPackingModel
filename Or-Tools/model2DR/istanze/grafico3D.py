#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[7]:


df = pd.read_excel('result.xlsx')


# In[8]:


print df.head()


# In[9]:


#df.drop('Eu Obj', axis =1, inplace=True)
#df.drop('Mod Obj', axis =1, inplace=True)

# In[10]:


threedee = plt.figure().gca(projection='3d')
threedee.scatter(df['Time'], df['equal'], df['n_items'])
threedee.set_xlabel('Time')
threedee.set_ylabel('equal')
threedee.set_zlabel('n_items')
plt.show()


# In[ ]:





# In[ ]:




