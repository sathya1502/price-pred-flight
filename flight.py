import pandas as pd
import seaborn as sns
import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder

st.title("Flight Price Prediction")
st.write("This project is deployed using flight Price Prediction Data set")

df=pd.read_csv('flight.csv')
le = LabelEncoder()

a=st.text_input("Airline",0)
le.fit_transform(df["Airline"])
x = le.transform([a])
st.write(x)
    
s=st.text_input("Source")
le.fit_transform(df['Source'])
source=le.transform([s])
st.write(source)

d=st.text_input("Destination",0)
le.fit_transform(df['Destination'])
dest=le.transform([d])
st.write(dest)

st.write("Duration")
hour= st.slider("Select the number of hours", 0, 100)
minutes= st.slider("Select the number of minutes", 0, 60)
duration = ((hour*60)+minutes)
st.write(duration)

st.write("Date of Journey")
month = st.slider("Select the month of Journey", 1, 12)
day = st.slider("Select the day of Journey", 1,31)

st.write("Departure Time")
dep_hr = st.slider("Select the hour of departure", 0, 100)
dep_min = st.slider("Select the minutes of departure", 0, 60)

st.write("Arrival Time")
arr_hr = st.slider("Select the hour of Arrival", 0, 100)
arr_min = st.slider("Select the minutes of Arrival", 0, 60)
   

    




with open('C:\\Users\\Sathya\\Documents\\GC\\Flight_Price_Pred\\ensembleb','rb') as file:
    pred=pickle.load(file)

result=pred.predict([[airline,source,dest,duration,month,day,dep_hr,dep_min,arr_hr,arr_min]])
st.write(result[0])

