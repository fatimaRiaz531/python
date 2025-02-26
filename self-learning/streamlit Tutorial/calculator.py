<<<<<<< HEAD
<<<<<<< HEAD
import streamlit as st

# Title of the app
st.title("Simple Calculator App")

# Sidebar for navigation or additional options (optional)
st.sidebar.header("Options")
st.sidebar.write("This is a simple calculator app built with Streamlit.")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown to select the operation
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Error: Division by zero!")

# Footer
st.markdown("---")
=======
=======
>>>>>>> 14b893526a3790dcb6be60b45ab67514288ea05d
import streamlit as st

# Title of the app
st.title("Simple Calculator App")

# Sidebar for navigation or additional options (optional)
st.sidebar.header("Options")
st.sidebar.write("This is a simple calculator app built with Streamlit.")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown to select the operation
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Error: Division by zero!")

# Footer
st.markdown("---")
<<<<<<< HEAD
>>>>>>> cf86935 (Fixed Streamlit deployment issue)
=======
>>>>>>> 14b893526a3790dcb6be60b45ab67514288ea05d
st.write("Made with ❤️ using Streamlit")