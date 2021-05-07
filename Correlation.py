#!/usr/bin/env python
# coding: utf-8

# In[6]:


#expt4_output
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler


# In[7]:


data_csv = pd.read_csv('C:\\Users\\admin\\Desktop\\Data Science\\engineering.csv')


# In[8]:


data_csv.describe()


# In[9]:


data_csv.describe(include="O")


# In[10]:


#CORRELATION
cor = data_csv.corr()
cor


# In[11]:


correlation = data_csv.corr()
sns.heatmap(correlation)


# In[12]:


#LINEAR CORRELATION 
plt.matshow(data_csv.corr())
plt.colorbar()
plt.show()


# In[13]:


#SPEARMAN METHOD OF CORRELATION
corr_matrix = data_csv.corr(method='spearman')
corr_matrix


# In[14]:


ax = plt.figure(figsize = (14,8))
ax = sns.heatmap(corr_matrix,cmap='PiYG')


# In[31]:


#PRINCIPLE COMPONENT ANALYSIS
data_csv.keys()


# In[36]:


df = data_csv[[ 'tlr', 'rpc', 'go', 'oi']].copy()
fea=[ 'tlr', 'rpc', 'go', 'oi']
x=data_csv.loc[:,fea].values
y=data_csv.loc[:,['tlr']].values
x=StandardScaler().fit_transform(x)
df.head(5)


# In[37]:


#STANDARDIZE THE DATA
scaler=StandardScaler()
scaler.fit(df)

scaled_data=scaler.transform(df)
scaled_data


# In[40]:


pca=PCA(n_components=2)
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)
scaled_data.shape
x_pca.shape
scaled_data
x_pca


# In[43]:


#VISUALISE 2D PROJECTION
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=data_csv['go'])
plt.xlabel('First principle component')
plt.ylabel('Second principle component')


# In[44]:


#pearson's coefficient
from scipy.stats import pearsonr


# In[45]:


pearsonc, _ = pearsonr(data_csv.tlr[0:100],data_csv.rpc[0:100])
print(pearsonc)


# In[ ]:


#positive value so that the positive correlation between tlr and rpc


# In[70]:


#CHI-SQUARE TEST
x=[]
y=[]
graduation_outcome = list(data_csv['go'])
teaching_learning = list(data_csv['tlr'])
for i in graduation_outcome:
    if i>70:
        x.append(i)
for i in teaching_learning:
    if i>70:
        y.append(i)


# In[67]:


m = min(len(x),len(y))
data =[x[0:m],y[0:m]]
stat, p, dof, expected = chi2_contingency(data) 
print(p)


# In[69]:


alpha = 2.5
if p<=alpha:
    print("Graduation Outcome is dependent on Teaching learning resource")
else:
    print("Graduation Outcome is dependent on Teaching learning resource")


# In[ ]:


#chi square test shows that GO is dependent on TLR

