import streamlit as st

# Title of the app
st.title("Unit Converter")

# Define conversion factors for different units
conversion_factors = {
    "Length": {
        "Meters to Feet": 3.28084,
        "Feet to Meters": 0.3048,
        "Kilometers to Miles": 0.621371,
        "Miles to Kilometers": 1.60934,
        "Centimeters to Meters": 0.01,  # Added
        "Meters to Centimeters": 100,   # Added
        "Centimeters to Inches": 0.393701,  # Added
        "Inches to Centimeters": 2.54,  # Added
    },
    "Weight": {
        "Kilograms to Pounds": 2.20462,
        "Pounds to Kilograms": 0.453592,
        "Grams to Ounces": 0.035274,
        "Ounces to Grams": 28.3495,
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9,
    }
}

# Sidebar for selecting the category
st.sidebar.header("Select Conversion Category")
category = st.sidebar.selectbox("Choose a category", list(conversion_factors.keys()))

# Get the available conversions for the selected category
conversions = conversion_factors[category]

# Main content
st.header(f"{category} Converter")

# Select the conversion type
conversion_type = st.selectbox("Select Conversion Type", list(conversions.keys()))

# Input value from the user
value = st.number_input("Enter the value to convert", value=1.0)

# Perform the conversion
if category == "Temperature":
    # Temperature conversions use lambda functions
    result = conversions[conversion_type](value)
else:
    # Other conversions use multiplication
    result = value * conversions[conversion_type]

# Display the result
st.subheader("Result")
st.write(f"{value} {conversion_type.split(' to ')[0]} = {result:.2f} {conversion_type.split(' to ')[1]}")

# Add a footer
st.markdown("---")  # Adds a horizontal line for separation
st.markdown("<h6 style='text-align: center; color: gray;'>Made by Fatima</h6>", unsafe_allow_html=True)