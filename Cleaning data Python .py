#!/usr/bin/env python
# coding: utf-8

# In[125]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[155]:


df =pd.read_csv(r"C:\Users\Admin\Desktop\Covid Project\Spotify_data.csv")


# In[156]:


df


# In[128]:


df = df.drop_duplicates()
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[117]:


df["Age"] = df["Age"].replace("35-60", np.nan)
df


# In[116]:


df = df.dropna(subset=["Age"])


# In[130]:


df["preffered_premium_plan"] = df["preffered_premium_plan"].replace("None, np.nan")
df = df.dropna(subset=["preffered_premium_plan"])
df


# In[131]:


df = df.drop(columns=["music_expl_method", "preffered_pod_format", "music_lis_frequency", "pod_host_preference", "preffered_pod_duration", "music_Influencial_mood"])
df


# In[ ]:


df = df.set_index ('Age')
grouped = df.groupby('Age')
df3


# In[ ]:


df.info()


# In[ ]:


df.describe()


# In[1]:


df.isnull().sum()


# In[ ]:


df.nunique()


# In[ ]:


df.groupby('Age').mean().sort_values(by="music_recc_rating",ascending=False)


# In[ ]:


df = df.transpose()
df


# In[ ]:


df.select_dtypes(include='object')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[154]:





# In[ ]:




