#!/usr/bin/env python
# coding: utf-8

# # Liver Disease predection

# In[1]:


#importing built in modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Loading Data
df=pd.read_csv(r"C:\Users\charan\Desktop\indian_liver_patient.csv")


# In[3]:


df.shape


# In[4]:


df.columns


# In[5]:


df.head()


# In[6]:


df.describe()


#  # pre-processing  data

# In[7]:


df.isnull().any().any()


# In[8]:


df.isnull().any()


# In[9]:


sns.countplot(data=df, x = 'Dataset', label='Count')

LD, NLD = df['Dataset'].value_counts()
print('Number of patients diagnosed with liver disease: ',LD)
print('Number of patients not diagnosed with liver disease: ',NLD)


# In[10]:


sns.countplot(data=df, x = 'Gender', label='Count')

F, M = df['Gender'].value_counts()
print('Number of patients that are female: ',M)
print('Number of patients that are male: ',F)


# In[11]:


# Create separate object for target variable
y = df.Dataset
# Create separate object for input features
df = df.drop('Dataset', axis=1)


# In[12]:


df.head()


# In[13]:


y.head()


# In[14]:


df_2=pd.get_dummies(df, columns=["Gender"],drop_first=False)
df_2


# In[ ]:





# In[ ]:





# ## Feature scalling

# In[15]:


# Scale down the values  using normalization between (0-1)
# Xnorm = (X-Xmin)/(Xmax-Xmin)

from sklearn import preprocessing
x=df_2.values
min_max_scaler=preprocessing.MinMaxScaler()   
x_scaled=min_max_scaler.fit_transform(x)
df=pd.DataFrame(x_scaled)


# In[16]:


df


# In[17]:


df.fillna(df.mean(),inplace=True)
df


# ### Splitting the data into training samples and testing samples

# In[18]:


X=df.values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)


# In[19]:


print("X-train =",X_train.shape,"  Y-train =", y_train.shape)
print("X-test  =", X_test.shape,"  Y-test  =", y_test.shape)


# # Logestic Regression

# In[20]:


#from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression(random_state=0,solver='lbfgs',multi_class='multinomial',max_iter=10000)
clf.fit(X_train,y_train)


# In[21]:


y_pred=clf.predict(X_test)


# In[22]:


y_pred


# In[23]:


y_test


# In[24]:


from sklearn import metrics
accuracy=metrics.accuracy_score(y_test,y_pred)
confusionmatrix=metrics.confusion_matrix(y_test,y_pred)
print("accuracy= ",round(accuracy,2))     # accuracy=no of correct predections/total no of predections made

print("Confusion matrix:\n", confusionmatrix)


# In[ ]:





# # KNN 

# In[25]:


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


# In[26]:


MSE


# In[27]:


cv_scores


# In[28]:


MSE.index(min(MSE))


# In[29]:


# plot misclassification error vs k 
plt.plot(neighbors, cv_scores)
plt.xlabel('Number of Neighbors K')
plt.ylabel('accuracy')
plt.show()


# In[30]:


# plot misclassification error vs k 
plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()


# In[31]:


classifier = KNeighborsClassifier(n_neighbors = optimal_k)
classifier.fit(X_train, y_train)


# In[32]:


y_pred = classifier.predict(X_test)


# In[33]:


acc = metrics.accuracy_score(y_test, y_pred) * float(100)  ## get the accuracy on testing data
print("accuracy= ",round(acc,2))


# In[34]:


cnf=metrics.confusion_matrix(y_test,y_pred)
print("Confusion matrix:\n", cnf)


# In[ ]:





# # Decision Tree 

# In[35]:


from sklearn.tree import DecisionTreeClassifier    # decision tree classifier using gini impurity (CART): 
dtclf=DecisionTreeClassifier() 
#dtclf=DecisionTreeClassifier(criterion='entropy') 
dtclf.fit(X_train,y_train)


# In[36]:


y_pred = dtclf.predict(X_test)


# In[37]:


acc = metrics.accuracy_score(y_test, y_pred) * float(100)  ## get the accuracy on testing data
print("accuracy= ",round(acc,2))


# In[38]:


cnf=metrics.confusion_matrix(y_test,y_pred)
print("Confusion matrix:\n", cnf)


# In[39]:


# from sklearn.externals.six import StringIO
# from IPython.display import Image
# from sklearn.tree import export_graphviz
# import pydotplus


# # Random forest

# In[40]:


from sklearn.ensemble import RandomForestClassifier
from math import sqrt
from sklearn.metrics import mean_squared_error
rfclf=RandomForestClassifier(n_estimators=100,max_depth=2,random_state=0)
rfclf.fit(X_train,y_train)
y_pred = rfclf.predict(X_test)


# In[41]:


acc = metrics.accuracy_score(y_test, y_pred) * float(100) 
print("accuracy= ",acc)


# In[42]:


mse=mean_squared_error(y_test, y_pred)   # mse=1/n(y-y^)^2
msd=sqrt(mse)
print("mean square error=",mse,"\nmean square deviation=",msd)


# In[ ]:





# # Navebias

# In[43]:


from sklearn.naive_bayes import MultinomialNB
#from sklearn.naive_bayes import CategoricalNB
from math import sqrt
from sklearn.metrics import mean_squared_error
nbclf=MultinomialNB()
nbclf.fit(X_train,y_train)
y_pred = nbclf.predict(X_test)


# In[44]:


acc = metrics.accuracy_score(y_test, y_pred) 
mse=mean_squared_error(y_test, y_pred) # mse=1/n(y-y^)^2
msd=sqrt(mse) 
print("accuracy= ",acc)
print("mean square error=",mse,"\nmean square deviation=",msd)


# # Suport vector machine

# In[45]:


from sklearn import svm
svmclf=svm.SVC(kernel='rbf',gamma='auto',decision_function_shape='ovo',probability=True)
svmclf.fit(X_train,y_train)
y_pred = svmclf.predict(X_test)


# In[46]:


acc = metrics.accuracy_score(y_test, y_pred)
print("accuracy= ",acc*100)


# In[47]:


cnf=metrics.confusion_matrix(y_test,y_pred)
print("Confusion matrix:\n", cnf)


# In[ ]:





# In[49]:


from sklearn.ensemble import GradientBoostingClassifier
# Create Gradient Boosting Classifier object
gbclass = GradientBoostingClassifier()
gbclass.fit(X_train, y_train)
#Predict Output
y_pred= gbclass.predict(X_test)
gbclass_score_test = round(gbclass.score(X_test, y_test) * 100, 2)
print('Test Score: \n', gbclass_score_test)
print('Accuracy: \n', round(metrics.accuracy_score(y_test,y_pred)*100,2))
print(metrics.confusion_matrix(y_pred,y_test))


# In[51]:


# Neural Networks# Neural 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

neural = MLPClassifier(max_iter=350)
neural.fit(X_train, y_train)
#Predict Output
y_pred = neural.predict(X_test)

neural_score_test = round(neural.score(X_test, y_test) * 100, 2)
print('Neural Test Score: \n', neural_score_test)
print('Accuracy: \n', accuracy_score(y_test, y_pred))
print(confusion_matrix(y_pred,y_test))


# In[ ]:





# In[ ]:





# In[ ]:


pickle.dump(clf,open('log.pkl','wb'))
pickle.dump(classifier,open('knn.pkl','wb'))
pickle.dump(dtclf,open('decisiontree.pkl','wb'))
pickle.dump(rfclf,open('randomforest.pkl','wb'))
pickle.dump(nbclf,open('navebais.pkl','wb'))
pickle.dump(svmclf,open('svm.pkl','wb'))
pickle.dump(gbclass,open('gb.pkl','wb'))
pickle.dump(neural,open('neural.pkl','wb'))


# In[ ]:





# In[ ]:





# In[ ]:




