import streamlit as st
from streamlit_option_menu import option_menu

# Function to add custom CSS
def add_custom_css():
    st.markdown("""
        <style>
            .main {
                background-color: #f5f5f5;
                padding: 20px;
            }
            .stButton button {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #0056b3;
            }
        </style>
    """, unsafe_allow_html=True)

# Adding custom CSS
add_custom_css()

# Title of the app
st.title("TORM Shipping Company - Ship Tracker")

# Sidebar menu for input
with st.sidebar:
    selected = option_menu("Main Menu", ["Ship Information", "Tracking Information"],
                           icons=['ship', 'map'], menu_icon="cast", default_index=0)

if selected == "Ship Information":
    st.header("Enter Ship Information")
    col1, col2 = st.columns(2)
    
    with col1:
        ship_name = st.text_input("Ship Name")
        imo_number = st.text_input("IMO Number")
        mmsi_number = st.text_input("MMSI Number")
    
    with col2:
        cargo_type = st.selectbox("Type of Cargo", ["Oil", "Gas", "Bulk", "Container", "Other"])
        ship_speed = st.number_input("Speed of Ship (knots)", min_value=0, max_value=100, value=0)
        crew_members = st.number_input("Number of Crew Members", min_value=0, max_value=1000, value=0)

    st.subheader("Entered Ship Information")
    st.write(f"**Ship Name:** {ship_name}")
    st.write(f"**IMO Number:** {imo_number}")
    st.write(f"**MMSI Number:** {mmsi_number}")
    st.write(f"**Type of Cargo:** {cargo_type}")
    st.write(f"**Speed of Ship:** {ship_speed} knots")
    st.write(f"**Number of Crew Members:** {crew_members}")

elif selected == "Tracking Information":
    st.header("Enter Tracking Information")
    
    start_port = st.text_input("Start Port")
    end_port = st.text_input("End Port")
    tracking_status = st.selectbox("Tracking Status", ["In Port", "At Sea", "Arrived"])

    st.subheader("Tracking Information")
    st.write(f"**Start Port:** {start_port}")
    st.write(f"**End Port:** {end_port}")
    st.write(f"**Tracking Status:** {tracking_status}")

# Optionally, you can add more functionality like database connection, real-time tracking, etc.
