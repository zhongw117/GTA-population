#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import pymysql.cursors


# In[4]:


connection = pymysql.connect(host='localhost', user='root', password='a', db='popu-gta', charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "SELECT district, Ppcount from GTApopulation where 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()


# In[5]:


# result


# In[6]:


pop_pd = pd.DataFrame(result)


# In[7]:


# pop_pd


# In[8]:

# f = plt.figure()
pop_pd.plot(kind='bar', x='district', y='Ppcount', figsize=(12,6))
plt.show()
# f.savefig("pop_hist.png")


# In[9]:


pop_pd.set_index('district', inplace=True)
# pop_pd


# In[10]:

# g = plt.figure()
pop_pd.plot.pie(x='distrct', y='Ppcount', figsize=(6,6))
plt.show()
# g.savefig("pop_pie.pdf")
plt.savefig('myfigure.jpg')


# In[ ]:
