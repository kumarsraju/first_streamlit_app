
import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My family Bakery')
streamlit.header('Cakes Menu')
streamlit.text('Chocolate')
streamlit.text('tres Les')
streamlit.text('Vanilla')
streamlit.text('Pineapple')

streamlit.header('BRUNCH MENU')
streamlit.text('🥣 Soup')
streamlit.text('🥗 Salad')
streamlit.text('🐔 Omlettes')
streamlit.text('🥑🍞 Avacado toast')

streamlit.dataframe(my_fruit_list)

