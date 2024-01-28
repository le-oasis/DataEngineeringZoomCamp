#!/usr/bin/env python
# coding: utf-8

# In[28]:


from sqlalchemy import create_engine
import pandas as pd
from time import time 


# In[29]:


df = pd.read_csv("data/green_tripdata_2019-09.csv", nrows=100)


# In[30]:


df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


# In[31]:


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()


# In[32]:


print(pd.io.sql.get_schema(df, name="green_taxi_data", con=engine))


# In[33]:


df_iter = pd.read_csv("data/green_tripdata_2019-09.csv", iterator=True, chunksize=100000)


# In[34]:


df = next(df_iter)


# In[35]:


len(df)


# In[36]:


df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


# In[37]:


df.info()


# In[38]:


df.head(n=0)


# In[39]:


df.head(n=0).to_sql(name="green_taxi_data",con=engine, if_exists='replace')


# In[40]:


get_ipython().run_line_magic('time', 'df.to_sql(name="green_taxi_data",con=engine, if_exists=\'append\')')


# In[41]:


while True:
    t_start = time()

    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.to_sql(name="green_taxi_data", con=engine, if_exists='append')

    t_end = time()

    print('Inserted another chunk.. took %.3f seconds' % (t_end - t_start))


# In[27]:


get_ipython().system(' wc -l "data/green_tripdata_2019-09.csv"')


# In[ ]:




