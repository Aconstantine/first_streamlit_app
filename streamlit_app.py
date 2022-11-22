import streamlit
import pandas as pd
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.header('Suck it')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt").set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
streamlit.text(fruityvice_response)
