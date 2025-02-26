import streamlit as st
import requests
from datetime import datetime, timedelta

def show_admin_page():
    if not st.session_state.get("logged_in"):
        st.warning("Please log in first")
        st.stop()
    
    st.title("Admin Dashboard")
    
    tabs = st.tabs(["Bookings", "Services", "Settings"])
    
    with tabs[0]:
        show_bookings()
    
    with tabs[1]:
        show_services()
    
    with tabs[2]:
        show_settings()

def show_bookings():
    st.header("Today's Bookings")
    # In real app, fetch from API
    bookings = [
        {"time": "09:00", "service": "Haircut", "client": "John"},
        {"time": "10:00", "service": "Coloring", "client": "Jane"}
    ]
    
    for booking in bookings:
        with st.expander(f"{booking['time']} - {booking['client']}"):
            st.write(f"Service: {booking['service']}")
            col1, col2 = st.columns(2)
            with col1:
                st.button("Complete", key=f"complete_{booking['time']}")
            with col2:
                st.button("Cancel", key=f"cancel_{booking['time']}")

def show_services():
    st.header("Manage Services")
    
    with st.form("add_service"):
        name = st.text_input("Service Name")
        duration = st.number_input("Duration (minutes)", min_value=15, step=15)
        price = st.number_input("Price ($)", min_value=0.0, step=5.0)
        
        if st.form_submit_button("Add Service"):
            # Here you would make API call to add service
            st.success("Service added successfully!")

def show_settings():
    st.header("Salon Settings")
    
    with st.form("salon_settings"):
        name = st.text_input("Salon Name", value="My Salon")
        address = st.text_area("Address", value="123 Main St")
        opening_time = st.time_input("Opening Time")
        closing_time = st.time_input("Closing Time")
        
        if st.form_submit_button("Save Settings"):
            # Here you would make API call to update settings
            st.success("Settings saved successfully!")

if __name__ == "__main__":
    show_admin_page() 