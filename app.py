import streamlit as st
import datetime
import requests

'''
# Welcome to NY Taxi Fare Estimator

Let's help you out estimating how much a taxi ride could cost.
'''

'''
## First let's start with some details:

'''



date_time = st.text_input('Date and time', value='')

pickup_lon = st.text_input('Pickup Longitude', value='')
pickup_lat = st.text_input('Pickup Latitude', value='')
dropoff_lon = st.text_input('Dropoff Longitude', value='')
dropoff_lat = st.text_input('Dropoff Latitude', value='')

passenger_count = st.text_input('Number of Passengers', value='')



'''


'''

url = 'https://first-container-ybocdqoiha-ew.a.run.app/predict_fare/'
# url = 'http://taxifare.lewagon.ai/predict_fare/'



'''

Click on the following button to get a prediction

'''


button = st.button('Predict!')




if button == True:
    # print is visible in server output, not in the page
    params = {
    'key': 1,
    'pickup_datetime': date_time,
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lon,
    'passenger_count': passenger_count
    } 
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        st.write('Check your details again. There might be something wrong.')
    else:
        st.write('Taxi fare would be around:')
        st.write(response.json()['prediction'])
    
   