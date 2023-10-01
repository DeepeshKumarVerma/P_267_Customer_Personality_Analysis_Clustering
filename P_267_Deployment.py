import pickle
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime,date

model = pickle.load(open('./random forest.pkl', 'rb'))
min_date = date(1920, 1, 1)
max_date=date.today()
martialstatusoptions = ["Alone", "Partner"]
educationOptions=["Basic","Graduation","Master","PhD"]

education=st.selectbox("Education",educationOptions)
marital_status=st.selectbox("Marital Status",martialstatusoptions)
income=st.number_input("Income")
kidhome=st.number_input("Kid Home")
Teenhome=st.number_input("Teen Home")
Recency=st.number_input("Recency")
MntWines=st.number_input("MntWines")
MntFruits=st.number_input("MntFruits")
MntMeatProducts=st.number_input("MntMeatProducts")
MntFishProducts=st.number_input("MntFishProducts")
MntSweetProducts=st.number_input("MntSweetProducts")
MntGoldProds=st.number_input("MntGoldProds")
NumDealsPurchases=st.number_input("NumDealsPurchases")
NumWebPurchases=st.number_input("NumWebPurchases")
NumCatalogPurchases=st.number_input("NumCatalogPurchases")
NumStorePurchases=st.number_input("NumStorePurchases")
NumWebVisitsMonth=st.number_input("NumWebVisitsMonth")
AcceptedCmp3=st.number_input("AcceptedCmp3")
AcceptedCmp4=st.number_input("AcceptedCmp4")
AcceptedCmp5=st.number_input("AcceptedCmp5")
AcceptedCmp1=st.number_input("AcceptedCmp1")
AcceptedCmp2=st.number_input("AcceptedCmp2")
Complain=st.number_input("Complain")
Response=st.number_input("Response")
Birthdate = st.date_input('Enter your birthdate:', min_value=min_date, max_value=max_date)

Year = st.number_input('Years_Registration', min_value=1, value=datetime.now().year)

Num_Accepted_Cmp=AcceptedCmp2+AcceptedCmp1+AcceptedCmp5+AcceptedCmp4+AcceptedCmp3
Num_Total_Purchases=NumWebPurchases+NumCatalogPurchases+NumStorePurchases
Sum_Mnt=MntWines+MntFruits+MntMeatProducts+MntFishProducts+MntSweetProducts+MntGoldProds

if st.button("Submit"):
    Age=datetime.now().year-Birthdate.year
    Years_Since_Registration=datetime.now().year-Year
    Education=0
    if education=="Basic":
        Education=0
    elif education=="Graduation":
        Education=1
    elif education=="Master":
        Education=2
    elif education=="PhD":
        Education=3
    Alone=0
    Partner=0
    Family_Size=0
    if marital_status=="Alone":
        Alone=1
        Family_Size=1

    elif marital_status=="Partner":
        Partner=1
        Family_Size=2
    
    Family_Size=Family_Size+kidhome+Teenhome
    minmaxscale = pickle.load(open('./minmax.pkl', 'rb'))
    data=[[Education,income,Recency,NumDealsPurchases,Complain,Response,Age,Years_Since_Registration,Family_Size,Alone,Partner,Sum_Mnt,Num_Accepted_Cmp,Num_Total_Purchases]]
    data=minmaxscale.transform(data)
    st.write(model.predict(data))



