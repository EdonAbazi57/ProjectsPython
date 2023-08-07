#!/usr/bin/env python
# coding: utf-8

# In[37]:


import os,shutil


# In[38]:


path = r"C:\Users\Admin\Desktop\Alex/"


# In[39]:


file_name = os.listdir(path)


# In[42]:


folder_names =['cvs files' ,'image files','text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))


# In[45]:


for file in file_name:
    if ".csv" in file and not os.path.exists(path +"csv files/"+file):
        shutil.move (path,file,path+"csv files/"+file)
    elif ".png" in file and not os.path.exists(path +"csv files/"+file):
        shutil.move (path,file,path+"csv files/"+file)
    elif ".txt" in file and not os.path.exists(path +"csv files/"+file):
        shutil.move (path,file,path+"csv files/"+file)
    else:
        print('there are file types in this path that were not moved')


# In[ ]:




