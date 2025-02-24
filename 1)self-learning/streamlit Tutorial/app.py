import streamlit as st

st.title("Streamlit  Turtorial")
# header
st.header("This is a header")
# sub header
st.subheader("This is a subheader")
#text
st.text("Hello World!!!!")
# mark down
st.markdown("### This is a markdown")
#error / colorful text
st.success("successful done")
# information
st.info("information")
#warning
st.warning("This is a warning")
#error
st.error("This is an error ")
#exception
# st.exception("NameError ('name 'rs' is not defined')")
#help

import pandas
st.help(pandas)

#range func
st.help(range)

#writing text super func
st.write("Text with write")
#range define

st.write(range(7))


# image
from PIL import Image
img = Image.open("pic.webp")
st.image(img)