import streamlit as st
import requests
from datetime import datetime, timedelta
import json
import plotly.graph_objects as go
import plotly.express as px
from time import sleep

# Page config must be the first streamlit command
st.set_page_config(page_title="Salon Booking System", page_icon="💇‍♀️", layout="wide")

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_type' not in st.session_state:
    st.session_state.user_type = None
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "wide"

# Custom CSS
st.markdown("""
<style>
    /* Base theme colors */
    :root {
        --primary-color: #FF4B4B;
        --secondary-color: #2E86C1;
        --background-color: #ffffff;
        --text-color: #1a1a1a;
        --card-bg: #ffffff;
        --blue-text: #2E86C1;  /* نیا نیلا رنگ */
    }

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Text colors - all white text changed to blue */
    .stMarkdown, .stText, p, span, div {
        color: var(--blue-text) !important;
    }

    /* Headers with stronger contrast */
    h1, h2, h3, h4, h5, h6 {
        color: #1a365d !important;  /* گہرا نیلا رنگ */
        font-weight: bold !important;
    }

    /* Cards styling */
    .salon-card {
        background-color: var(--card-bg);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border: 1px solid #e1e4e8;
    }

    .salon-card h3 {
        color: #2C3E50 !important;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }

    .salon-card h2 {
        color: var(--primary-color) !important;
        font-size: 2rem;
        font-weight: bold;
    }

    /* Buttons - changed white text to blue */
    .stButton button {
        background: linear-gradient(45deg, var(--primary-color), #FF7676);
        color: var(--blue-text) !important;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        background: linear-gradient(45deg, #FF7676, var(--primary-color));
    }

    /* Form inputs */
    .stTextInput input, .stTextArea textarea, .stDateInput input {
        color: var(--blue-text) !important;
        border-color: var(--blue-text) !important;
    }

    /* Calendar styling - changed white text to blue */
    .calendar-table th {
        background-color: var(--primary-color);
        color: var(--blue-text) !important;
        padding: 12px;
        text-align: center;
        font-weight: bold;
    }

    .calendar-table td {
        padding: 12px;
        text-align: center;
        border: 1px solid #e1e4e8;
        color: #2C3E50;
    }

    /* Tabs styling - changed white text to blue */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: white;
        border-radius: 5px 5px 0 0;
        gap: 1px;
        padding: 10px 20px;
        color: #2C3E50;
    }

    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: var(--primary-color);
        color: var(--blue-text) !important;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: white;
    }

    /* Charts */
    .js-plotly-plot {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }

    /* Calendar day highlight - changed white text to blue */
    td[style*="background: #FF4B4B"] {
        color: var(--blue-text) !important;
    }

    /* Make form labels visible */
    .stSelectbox label, .stSlider label, .stDateInput label {
        color: var(--blue-text) !important;
    }

    /* Make sidebar text visible */
    .css-1d391kg, .css-1d391kg p {
        color: var(--blue-text) !important;
    }

    /* Make chart text visible */
    .js-plotly-plot text {
        fill: var(--blue-text) !important;
    }

    /* Ensure notification text is visible */
    .stToast {
        color: var(--blue-text) !important;
    }
</style>
""", unsafe_allow_html=True)

def display_booking(booking):
    """Helper function to display a booking"""
    with st.container():
        st.markdown(f"""
        <div class="salon-card">
            <h4>{booking['time']} - {booking['client']}</h4>
            <p>Service: {booking['service']}</p>
            <p>Duration: {booking['duration']} minutes</p>
        </div>
        """, unsafe_allow_html=True)

def login_page():
    st.title("💇‍♀️ Salon Booking System")
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.header("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            # Here you would validate with your backend
            st.session_state.logged_in = True
            st.session_state.user_type = "salon"
            st.rerun()
            
    with tab2:
        st.header("Register Salon")
        salon_name = st.text_input("Salon Name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_pass")
        address = st.text_area("Address")
        
        if st.button("Register"):
            st.success("Registration successful! Please login.")

def salon_dashboard():
    # Show loading spinner
    with st.spinner('Loading dashboard...'):
        sleep(1)  # Simulate loading
        st.success('Welcome to your dashboard!')
    
    # Progress bar example
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        sleep(0.01)
    
    st.title("Salon Dashboard")
    
    # Add summary cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="salon-card">
            <h3>Today's Bookings</h3>
            <h2>8</h2>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="salon-card">
            <h3>Revenue Today</h3>
            <h2>$450</h2>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="salon-card">
            <h3>Active Services</h3>
            <h2>12</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # View mode selector
    st.sidebar.markdown("### View Settings")
    if st.sidebar.checkbox("Compact View", value=(st.session_state.view_mode == "centered")):
        st.session_state.view_mode = "centered"
    else:
        st.session_state.view_mode = "wide"
    
    tab1, tab2, tab3 = st.tabs(["Bookings", "Services", "Settings"])
    
    with tab1:
        st.header("Bookings Calendar")
        # Create a simple HTML calendar
        calendar_html = """
        <div style="padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h3>March 2024</h3>
            <table class="calendar-table">
                <tr>
                    <th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th>
                </tr>
                <tr>
                    <td></td><td></td><td></td><td></td><td></td><td>1</td><td>2</td>
                </tr>
                <tr>
                    <td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td>
                </tr>
                <tr>
                    <td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td>
                </tr>
                <tr>
                    <td>17</td><td>18</td><td>19</td>
                    <td style="background: #FF4B4B; color: white; border-radius: 5px;">20</td>
                    <td>21</td><td>22</td><td>23</td>
                </tr>
                <tr>
                    <td>24</td><td>25</td><td>26</td><td>27</td><td>28</td><td>29</td><td>30</td>
                </tr>
                <tr>
                    <td>31</td><td></td><td></td><td></td><td></td><td></td><td></td>
                </tr>
            </table>
            <div style="margin-top: 10px;">
                <p><span style="background: #FF4B4B; color: white; padding: 2px 5px; border-radius: 3px;">20</span> - Booked appointments</p>
            </div>
        </div>
        """
        st.markdown(calendar_html, unsafe_allow_html=True)
        
        # Add booking timeline
        bookings = [
            {"time": "09:00", "service": "Haircut", "client": "John Doe", "duration": 60},
            {"time": "10:30", "service": "Coloring", "client": "Jane Smith", "duration": 90}
        ]

        fig = go.Figure()
        for booking in bookings:
            fig.add_trace(go.Bar(
                x=[booking['duration']],
                y=[booking['time']],
                orientation='h',
                name=f"{booking['client']} - {booking['service']}",
                hoverinfo='text',
                text=f"{booking['client']} - {booking['service']}"
            ))
        
        fig.update_layout(
            title="Today's Schedule",
            xaxis_title="Duration (minutes)",
            yaxis_title="Time",
            barmode='stack'
        )
        st.plotly_chart(fig)

        # Display bookings in responsive columns
        st.subheader("Today's Bookings")
        for i in range(0, len(bookings), 2):
            col1, col2 = st.columns(2)
            with col1:
                display_booking(bookings[i])
            if i + 1 < len(bookings):
                with col2:
                    display_booking(bookings[i + 1])
    
    with tab2:
        st.header("Service Analytics")
        
        # Interactive date range selector
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date")
        with col2:
            end_date = st.date_input("End Date")
            
        # Interactive filters
        service_filter = st.multiselect(
            "Select Services",
            ["Haircut", "Coloring", "Styling", "Massage"],
            default=["Haircut", "Coloring"]
        )
        
        # Interactive slider
        price_range = st.slider(
            "Price Range",
            min_value=0,
            max_value=200,
            value=(20, 100)
        )
        
        # Add service popularity chart
        service_data = {
            'Service': ['Haircut', 'Coloring', 'Styling', 'Massage'],
            'Bookings': [45, 30, 25, 20]
        }
        fig = px.pie(service_data, values='Bookings', names='Service', title='Service Popularity')
        st.plotly_chart(fig)
        
        # Service management form
        with st.form("add_service"):
            service_name = st.text_input("Service Name")
            duration = st.number_input("Duration (minutes)", min_value=15, step=15)
            price = st.number_input("Price ($)", min_value=0.0, step=5.0)
            if st.form_submit_button("Add Service"):
                st.success("Service added successfully!")
    
    with tab3:
        st.header("Salon Settings")
        st.text_input("Salon Name", value="My Salon")
        st.text_area("Address", value="123 Main St")
        st.time_input("Opening Time")
        st.time_input("Closing Time")
        if st.button("Save Settings"):
            st.success("Settings saved successfully!")

    # Notification demo
    if st.button('Show Notification'):
        st.balloons()
        st.toast('This is a notification!', icon='🔔')
    
    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_type = None
        st.rerun()

def main():
    if not st.session_state.logged_in:
        login_page()
    elif st.session_state.user_type == "salon":
        salon_dashboard()

if __name__ == "__main__":
    main()