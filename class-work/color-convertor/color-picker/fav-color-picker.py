import streamlit as st

# Title of the app
st.title("🎨 Favorite Color Picker")

# Input fields with unique keys
name = st.text_input("Enter your name:", placeholder="Your name here", key="name_input")
favorite_color = st.selectbox("Choose your favorite color:", ["Red", "Green", "Blue", "Yellow", "Purple"], key="color_input")

# Display the result
if name and favorite_color:
    st.write(f"Hello, **{name}**! Your favorite color is **{favorite_color.lower()}**.")
    st.markdown(
        f"<h1 style='color:{favorite_color.lower()};'>This text is in your favorite color!</h1>",
        unsafe_allow_html=True
    )
