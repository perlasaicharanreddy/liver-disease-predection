#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pickle


log=pickle.load(open('log.pkl','rb'))
knn=pickle.load(open('knn.pkl','rb'))
decisiontree=pickle.load(open('decisiontree.pkl','rb'))
randomforest=pickle.load(open('randomforest.pkl','rb'))
naivebayes=pickle.load(open('navebais.pkl','rb'))
svm=pickle.load(open('svm.pkl','rb'))



def classify(num):
    if num==1: return "The Patient has liver disease";
    else: return "The Patient has dont liver disease";

def main():
    st.title("Liver disease Predection")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Liver disease Predection</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Logistic Regression','KNN','Decision tree','Random forest','naive bayes','SVM']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    
    age=st.text_input("Enter  age")
    gender = st.radio("Gender",("Male","Female"))
    Total_Bilirubin=st.slider('Total_Bilirubin', 0.0, 75.0)
    Direct_Bilirubin=st.slider('Direct_Bilirubin', 0.0, 20.0)
    Alkaline_Phosphotase=st.slider('Alkaline_Phosphotase ', 0.0, 2100.0)
    Alamine_Aminotransferase=st.slider('Alamine_Aminotransferase ', 0.0, 2000.0)
    Aspartate_Aminotransferase=st.slider('Aspartate_Aminotransferase ', 0.0, 5000.0)
    Total_Protiens=st.slider('Total_Protiens ', 0.0, 10.0)
    Albumin=st.slider('Albumin ', 0.0, 6.0)
    Albumin_and_Globulin_Ratio=st.slider('Albumin_and_Globulin_Ratio ', 0.0, 5.0)
    
    if gender=="Female":
        gender1=1
        gender2=0
    else:
        gender1=0
        gender2=1
    
    
    inputs=[[age,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,
             Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio,gender1,gender2]]
    
    if st.button('Classify'):
        if option=='Logistic Regression':
            st.success(classify(log.predict(inputs)))
        elif option=='KNN':
            st.success(classify(knn.predict(inputs)))
        elif option=='Decision tree':
            st.success(classify(decisiontree.predict(inputs)))
        elif option=='Random forest':
            st.success(classify(randomforest.predict(inputs)))
        elif option=='naive bayes':
            st.success(classify(naivebayes.predict(inputs)))
        else:
            st.success(classify(svm.predict(inputs)))


if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




