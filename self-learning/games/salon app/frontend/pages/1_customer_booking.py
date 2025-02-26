import streamlit as st
import requests
from datetime import datetime, timedelta

def show_booking_page():
    st.title("Book Your Appointment")
    
    # Get salon details from URL parameter
    salon_id = st.experimental_get_query_params().get("salon", ["1"])[0]
    
    # Fetch salon details and services
    # In real app, these would come from API
    services = [
        {"id": 1, "name": "Haircut", "duration": 30, "price": 30},
        {"id": 2, "name": "Coloring", "duration": 90, "price": 100},
    ]
    
    # Service selection
    selected_service = st.selectbox(
        "Choose Service",
        options=services,
        format_func=lambda x: f"{x['name']} (${x['price']})"
    )
    
    # Date selection
    date = st.date_input("Select Date")
    
    # Time selection
    available_times = ["09:00", "10:00", "11:00", "14:00", "15:00"]
    time = st.selectbox("Select Time", available_times)
    
    # Customer details
    with st.form("booking_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        
        if st.form_submit_button("Book Appointment"):
            if name and email:
                # Here you would make API call to create booking
                st.success("Booking successful! Check your email for confirmation.")
            else:
                st.error("Please fill in all fields")

if __name__ == "__main__":
    show_booking_page() 