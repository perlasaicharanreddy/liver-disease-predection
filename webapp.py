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



def classify(num,t):
    if (num==1 and t==1): return "The Patient is likely has liver disease";
    else : return "The Patient  is likely not having liver disease";

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
    
    age=st.slider("Enter  age",1,100)
    gender = st.radio("Gender",("Male","Female"))
    Total_Bilirubin=st.slider('Total_Bilirubin', 0, 75)
    Direct_Bilirubin=st.slider('Direct_Bilirubin', 0, 20)
    Alkaline_Phosphotase=st.slider('Alkaline_Phosphotase ', 0, 2100)
    Alamine_Aminotransferase=st.slider('Alamine_Aminotransferase ', 0, 2000)
    Aspartate_Aminotransferase=st.slider('Aspartate_Aminotransferase ', 0, 5000)
    Total_Protiens=st.slider('Total_Protiens ', 0, 10)
    Albumin=st.slider('Albumin ', 0, 6)
    Albumin_and_Globulin_Ratio=st.slider('Albumin_and_Globulin_Ratio ', 0, 5)
    
    if gender=="Female":
        gender1=1
        gender2=0
    else:
        gender1=0
        gender2=1
    
    
    inputs=[[age,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,
             Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio,gender1,gender2]]
    t=Total_Bilirubin>50 and (age!=0 and Total_Bilirubin!=0 and Direct_Bilirubin!=0 and Alkaline_Phosphotase!=0
                           and Aspartate_Aminotransferase!=0 and Total_Protiens!=0 and Albumin!=0 and Albumin_and_Globulin_Ratio!=0)
    if st.button('Classify'):
        if option=='Logistic Regression':
            st.success(classify(log.predict(inputs),t))
        elif option=='KNN':
            st.success(classify(knn.predict(inputs),t))
        elif option=='Decision tree':
            st.success(classify(decisiontree.predict(inputs),t))
        elif option=='Random forest':
            st.success(classify(randomforest.predict(inputs),t))
        elif option=='naive bayes':
            st.success(classify(naivebayes.predict(inputs),t))
        else:
            st.success(classify(svm.predict(inputs),t))


if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




