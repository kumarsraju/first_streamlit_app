import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# ------------------------------------------------------------------------------------- //
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) #normalize pandas data
  return fruityvice_normalized
# ------------------------------------------------------------------------------------- //
#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit for info.")
  else:
    val_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(val_from_function)
except URLError as e:
  streamlit.error()
  

#stop here to troubleshoot
streamlit.stop()
# ------------------------------------------------------------------------------------- //

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list");
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit Load List Has:")
streamlit.dataframe(my_data_row)

fruit_include = streamlit.text_input('What fruit should be added?')
streamlit.write('Thanks for adding', fruit_include)
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values (fruit_include)");
                     
