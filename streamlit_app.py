
import streamlit
import pandas


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


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Banana'])

# Display the table on the page.

streamlit.dataframe(my_fruit_list)

