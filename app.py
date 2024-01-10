import streamlit as st

st.title('Hihi')
st.title('Here is :violet[Xiran Lin] :sunglasses:')



st.subheader('About', divider='gray')
st.text('A product designer with entrepreneurship and passion for social good and smart things.')

st.subheader('Education')
st.text('B.A in Industrial Design')
st.subheader('Work Experience')
st.text('Work in Fabrie,Envision Digital,Shenzhen InnoX Academy,Midea Real Estate')
st.subheader('Hobbies and Interests')
st.text('Badminton, Hiking, Drama, Movie, Chinese Poem, Table Games')
st.subheader('Interests')
st.text('Human-Ai Interaction, Implicit Interaction, Calm Technology, Ubicomp, Inclusive Design')

col1, col2 = st.columns(2)
col1.image('image/IMG2.JPG', caption='Xiran Lin')


#1. A profile picture
#2. About
#3. Education
#4. Work Experience
#5. Hobbies and Interests
#6. Interesting Projects