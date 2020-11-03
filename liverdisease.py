#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Logestic Regression correct


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv(r"C:\Users\charan\Desktop\indian_liver_patient.csv")


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.head()


# In[7]:


df.describe()


# In[8]:


df.isnull().any().any()


# In[9]:


df.isnull().any()


# In[10]:


sns.countplot(data=df, x = 'Dataset', label='Count')

LD, NLD = df['Dataset'].value_counts()
print('Number of patients diagnosed with liver disease: ',LD)
print('Number of patients not diagnosed with liver disease: ',NLD)


# In[11]:


sns.countplot(data=df, x = 'Gender', label='Count')

F, M = df['Gender'].value_counts()
print('Number of patients that are female: ',M)
print('Number of patients that are male: ',F)


# In[12]:


import seaborn as sns
sns.pairplot(df,hue='Dataset')
#sns.pairplot(df,hue='Dataset',x_vars=['Age','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Albumin_and_Globulin_Ratio','Gender_Female','Gender_Male'],y_vars=['Dataset'])


# In[13]:


# Create separate object for target variable
y = df.Dataset
# Create separate object for input features
df = df.drop('Dataset', axis=1)


# In[14]:


df.head()


# In[15]:


y.head()


# In[16]:


df_2=pd.get_dummies(df, columns=["Gender"],drop_first=False)
df_2


# In[ ]:





# In[ ]:





# In[ ]:





# In[17]:


# Scale down the values  using normalization between (0-1)
# Xnorm = (X-Xmin)/(Xmax-Xmin)

from sklearn import preprocessing
x=df_2.values
min_max_scaler=preprocessing.MinMaxScaler()   
x_scaled=min_max_scaler.fit_transform(x)
df=pd.DataFrame(x_scaled)


# In[18]:


df


# In[19]:


df.fillna(df.mean(),inplace=True)
df


# In[ ]:





# In[20]:


X=df.values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)


# In[21]:


print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# In[22]:


from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression(random_state=0,solver='lbfgs',multi_class='multinomial',max_iter=10000)
clf.fit(X_train,y_train)


# In[23]:


clf.score(X_test,y_test)


# In[24]:


y_pred=clf.predict(X_test)


# In[25]:


y_pred


# In[26]:


s=y_test
s


# In[27]:


from sklearn import metrics
accuracy=metrics.accuracy_score(y_test,y_pred)
confusionmatrix=metrics.confusion_matrix(y_test,y_pred)
print("accuracy",accuracy)     # accuracy=no of correct predections/total no of predections made
print("confusion matrix\n",confusionmatrix) #


# In[28]:


# Logestic Regression end


# In[29]:


# KNN Start


# In[30]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# creating odd list of K for KNN
neighbors = list(range(1,20,2))
# empty list that will hold cv scores
cv_scores = []

#  10-fold cross validation , 9 datapoints will be considered for training and 1 for cross validation (turn by turn) to determine value of k
for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())   

# changing to misclassification error
MSE = [1 - x for x in cv_scores]

# determining best k
optimal_k = neighbors[MSE.index(min(MSE))]
print('\nThe optimal number of neighbors is %d.' % optimal_k)


# In[31]:


MSE


# In[32]:


cv_scores


# In[33]:


MSE.index(min(MSE))


# In[34]:


# plot misclassification error vs k 
plt.plot(neighbors, cv_scores)
plt.xlabel('Number of Neighbors K')
plt.ylabel('accuracy')
plt.show()


# In[35]:


# plot misclassification error vs k 
plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()


# In[36]:


classifier = KNeighborsClassifier(n_neighbors = optimal_k)
classifier.fit(X_train, y_train)


# In[37]:


y_pred = classifier.predict(X_test)


# In[38]:


acc = metrics.accuracy_score(y_test, y_pred) * float(100)  ## get the accuracy on testing data
acc


# In[39]:


cnf=metrics.confusion_matrix(y_test,y_pred)
cnf


# In[40]:


#knn end


# In[41]:


#decision tree classifier using gini impurity (CART): 


# In[42]:


from sklearn.tree import DecisionTreeClassifier
dtclf=DecisionTreeClassifier() 
#dtclf=DecisionTreeClassifier(criterion='entropy') 
dtclf.fit(X_train,y_train)


# In[43]:


y_pred = dtclf.predict(X_test)


# In[44]:


acc = metrics.accuracy_score(y_test, y_pred) * float(100)  ## get the accuracy on testing data
acc


# In[45]:


cnf=metrics.confusion_matrix(y_test,y_pred)
print(cnf)


# In[46]:


# from sklearn.externals.six import StringIO
# from IPython.display import Image
# from sklearn.tree import export_graphviz
# import pydotplus


# In[47]:


#Random forest


# In[48]:


from sklearn.ensemble import RandomForestClassifier
from math import sqrt
from sklearn.metrics import mean_squared_error
rfclf=RandomForestClassifier(n_estimators=100,max_depth=2,random_state=0)
rfclf.fit(X_train,y_train)
y_pred = rfclf.predict(X_test)


# In[49]:


acc = metrics.accuracy_score(y_test, y_pred) * float(100) 
acc


# In[50]:


mse=mean_squared_error(y_test, y_pred)   # mse=1/n(y-y^)^2
msd=sqrt(mse)
print(mse,msd)


# In[ ]:





# In[51]:


#Navebias


# In[52]:


from sklearn.naive_bayes import MultinomialNB
#from sklearn.naive_bayes import CategoricalNB
from math import sqrt
from sklearn.metrics import mean_squared_error
nbclf=MultinomialNB()
nbclf.fit(X_train,y_train)
y_pred = nbclf.predict(X_test)


# In[53]:


acc = metrics.accuracy_score(y_test, y_pred) 
mse=mean_squared_error(y_test, y_pred) # mse=1/n(y-y^)^2
msd=sqrt(mse) 
print(acc,mse,msd)


# In[54]:


#Suport vector machine


# In[55]:


from sklearn import svm
svmclf=svm.SVC(kernel='rbf',gamma='auto',probability=True)
svmclf.fit(X_train,y_train)
y_pred = svmclf.predict(X_test)


# In[56]:


acc = metrics.accuracy_score(y_test, y_pred)
acc


# In[ ]:





# In[57]:


#import seaborn as sns
#sns.pairplot(df,hue='Dataset')


# In[58]:


import pickle
#pickle.dump(clf,open('log.pkl','wb'))
#model=pickle.load(open('model.pkl','rb'))


# In[59]:


pickle.dump(clf,open('log.pkl','wb'))
pickle.dump(classifier,open('knn.pkl','wb'))
pickle.dump(dtclf,open('decisiontree.pkl','wb'))
pickle.dump(rfclf,open('randomforest.pkl','wb'))
pickle.dump(nbclf,open('navebais.pkl','wb'))
pickle.dump(svmclf,open('svm.pkl','wb'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




