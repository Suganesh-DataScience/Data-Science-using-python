#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


# In[2]:


df = pd.read_csv('C:\\Users\\ramur\\Documents\\Data science using python\\engineering.csv')


# In[3]:


df.head()


# In[4]:


df.dtypes


# In[5]:


df.isna().sum()


# In[6]:


df=df.fillna(0)


# In[7]:


df.isna().sum()


# In[8]:


le = LabelEncoder()


# In[9]:


le.fit(df.tlr.drop_duplicates())


# In[10]:


df.tlr = le.transform(df.tlr)


# In[11]:


le.fit(df.rpc.drop_duplicates())


# In[12]:


df.rpc = le.transform(df.rpc)


# In[13]:


le.fit(df.go.drop_duplicates())


# In[14]:


df.go = le.transform(df.go)


# In[15]:


le.fit(df.oi.drop_duplicates())


# In[16]:


df.oi = le.transform(df.oi)


# In[17]:


le.fit(df.perception.drop_duplicates())


# In[18]:


df.perception = le.transform(df.perception)


# In[20]:


df.head()


# In[34]:


x=df.drop(['institute_id','name','city','state'], axis=1)


# In[137]:


y=df['go']


# In[138]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)


# In[139]:


x_train


# In[140]:


y_train


# In[141]:


from sklearn.decomposition import PCA


# In[142]:


pca=PCA(n_components=2)


# In[143]:


pca.fit(x_train)



# In[144]:


x_pca=pca.transform(x_train)


# In[145]:


x_train.shape


# In[146]:


x_pca.shape


# In[147]:


plt.figure(figsize=(5,4))
plt.scatter(x_pca[:,0],x_pca[:,1],c=y_train)
plt.xlabel('PCA1')
plt.ylabel('PCA2')


# In[148]:


logreg = LogisticRegression(solver='liblinear', random_state=0)


# In[149]:


logreg.fit(x_pca, y_train)
x_te=pca.fit_transform(x_test)
y_pred_test=logreg.predict(x_te)
print('MODEL ACCURACY SCORE:{0:0.4f}'.format(accuracy_score(y_test,
y_pred_test)))


# In[150]:


from sklearn.decomposition import TruncatedSVD


# In[151]:


svd = TruncatedSVD(n_components=2)


# In[152]:


x_sv=svd.fit_transform(x_train)


# In[153]:


logreg = LogisticRegression(solver='liblinear', random_state=0)


# In[128]:


logreg.fit(x_sv, y_train)


# In[129]:


x_te=svd.fit_transform(x_test)


# In[130]:


y_pred_test=logreg.predict(x_te)


# In[131]:


print('MODEL ACCURACY SCORE:{0:0.4f}'.format(accuracy_score(y_test,
y_pred_test)))


# In[ ]:




