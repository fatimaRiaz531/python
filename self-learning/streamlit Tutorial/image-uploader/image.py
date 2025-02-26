# pip install pillow     yeh install krna h 
# pip install streamlit  yeh b har jagah install krna lazmi h 


import streamlit as st
from PIL import Image
import numpy as np

# Title of the app
st.title("Image Upload and Processing App")

# Sidebar for navigation or additional options (optional)
st.sidebar.header("Options")
st.sidebar.write("Upload an image and optionally convert it to grayscale.")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Option to convert the image to grayscale
    if st.checkbox("Convert to Grayscale"):
        grayscale_image = image.convert("L")
        st.image(grayscale_image, caption="Grayscale Image", use_column_width=True)

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")