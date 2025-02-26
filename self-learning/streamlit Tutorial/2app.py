<<<<<<< HEAD
import streamlit as st

st.title("Web App")
from PIL import Image
img = Image.open("pic.webp")
st.image(img, width=300, caption = "simple pic")
#video
vid_file = open("video.mp4", "rb")
vid_player = vid_file.read()
st.video(vid_player)
# audio 
studio_file = open("tune.mp3", "rb").read()
st.audio(studio_file)
#gender
if st.checkbox("show / hide "):
    st.text("showing or  hiding")
# radio buttons
status = st.radio("What is your status",( "active", "inactive") ) 

#link 
# if status == "Active":
#     st.success("you are active")

    #else func

if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive , Activate it")

#selectbox
occupation= st.selectbox("Your occupation", ("programmer", " dr", "teacher"))
st.write("you selected this occupation")

# multi  select
location = st.multiselect("where do you work",("karachi", "lahore", " Isl"))




=======
import streamlit as st

st.title("Web App")
from PIL import Image
img = Image.open("pic.webp")
st.image(img, width=300, caption = "simple pic")
#video
vid_file = open("video.mp4", "rb")
vid_player = vid_file.read()
st.video(vid_player)
# audio 
studio_file = open("tune.mp3", "rb").read()
st.audio(studio_file)
#gender
if st.checkbox("show / hide "):
    st.text("showing or  hiding")
# radio buttons
status = st.radio("What is your status",( "active", "inactive") ) 

#link 
# if status == "Active":
#     st.success("you are active")

    #else func

if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive , Activate it")

#selectbox
occupation= st.selectbox("Your occupation", ("programmer", " dr", "teacher"))
st.write("you selected this occupation")

# multi  select
location = st.multiselect("where do you work",("karachi", "lahore", " Isl"))




>>>>>>> 72242252ca52e2a3ce0a854d7db6213a49d226ab
