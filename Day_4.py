import streamlit as st

st.set_page_config(page_title = "test")
st.markdown('# This is the main page...')
st.sidebar.write('main page')
st.write("Hello guys. How are you today?")
st.write("How do i stop this session")
st.write("try again")
st.write("This is how you link to streamlit")
st.write("if you want to stop the program in terminal press button ctrl+c")
st.write("in streamlit setting, you already run on save, means that if your code saved while this program still run, the output popout in streramlit")
st.write(7+9/2)

st.header("this is header")
st.subheader("this is subheader")
st.caption("this is caption")

st.markdown("*Streamlit* is **really** ***welcome***")
st.markdown(''' :red[Streamlit] :orange[is] :green[fun]''')
st.markdown("Here's a bouquet $mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">This is advanced font manipulation!</p>' 
st.markdown(new_title, unsafe_allow_html=True) 

st.selectbox("Kuala Lumpur is located at", ['Malaysia', 'Thailand', 'UK'])
st.multiselect("Select 2 states", ['Selangor','Johor','Kedah'])

st.button("Click Here to Proceed")
st.slider("Select the length of stay", 1,10, value=3)

st.markdown("<h1 style='color:blue;'>Hello, Streamlit!</h1>", unsafe_allow_html=True)
st.markdown("<p>This is a paragraph in <b>bold</b> and <i>italic</i>.</p>", unsafe_allow_html=True)

number = st.number_input("Insert a number",value=None, placeholder="Type a number...")
st.write("The current number is ", number)

from PIL import Image 
im = Image.open('shrdc_logo.png')
st.image(im, width=300)

import pandas as pd
df = pd.read_excel('sampleData.xlsx')
df

st.dataframe(df)

st.bar_chart(df, x="Location", y="Income")

st.line_chart(df, x = 'Household', y = 'Income')

st.scatter_chart(df, x="Household", y="Income")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
 st.header("A cat")
 st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
 st.header("An owl")
 st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

col1, col2, col3 = st.columns(3)
with col1:
 st.header("A cat")
 st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
 st.header("An owl")
 st.image("https://static.streamlit.io/examples/owl.jpg")

