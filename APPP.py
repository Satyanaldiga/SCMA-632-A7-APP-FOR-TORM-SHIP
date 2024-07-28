import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

# Function to add custom CSS
def add_custom_css():
    st.markdown("""
        <style>
            .main {
                background-color: black;
                padding: 20px;
            }
            .stButton button {
                background-color: black;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: black;
            }
        </style>
    """, unsafe_allow_html=True)

# Adding custom CSS
add_custom_css()

# Initialize session state for ship data
if 'ship_data' not in st.session_state:
    st.session_state.ship_data = []

# Title of the app
st.title("TORM Shipping Company - Ship Tracker")

# Sidebar menu for input
with st.sidebar:
    selected = option_menu("Main Menu", ["Ship Information", "Tracking Information", "Data Visualization"],
                           icons=['ship', 'map', 'bar-chart'], menu_icon="cast", default_index=0)

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

    if st.button("Submit Ship Information"):
        st.session_state.ship_data.append({
            "Ship Name": ship_name,
            "IMO Number": imo_number,
            "MMSI Number": mmsi_number,
            "Type of Cargo": cargo_type,
            "Speed of Ship": ship_speed,
            "Number of Crew Members": crew_members,
            "Status": "Unknown",
            "Start Port": "",
            "End Port": ""
        })
        st.success("Ship information submitted!")

    st.subheader("Entered Ship Information")
    st.write(f"**Ship Name:** {ship_name}")
    st.write(f"**IMO Number:** {imo_number}")
    st.write(f"**MMSI Number:** {mmsi_number}")
    st.write(f"**Type of Cargo:** {cargo_type}")
    st.write(f"**Speed of Ship:** {ship_speed} knots")
    st.write(f"**Number of Crew Members:** {crew_members}")

elif selected == "Tracking Information":
    st.header("Enter Tracking Information")
    
    ship_search = st.text_input("Enter Ship Name to Search")
    if ship_search:
        ship_found = False
        for ship in st.session_state.ship_data:
            if ship["Ship Name"].lower() == ship_search.lower():
                ship_found = True
                st.subheader("Tracking Information for " + ship["Ship Name"])
                st.write(f"**Start Port:** {ship['Start Port']}")
                st.write(f"**End Port:** {ship['End Port']}")
                st.write(f"**Tracking Status:** {ship['Status']}")
                break
        if not ship_found:
            st.error("Ship not found. Please check the ship name.")

    start_port = st.text_input("Start Port")
    end_port = st.text_input("End Port")
    tracking_status = st.selectbox("Tracking Status", ["In Port", "At Sea", "Arrived"])

    if st.button("Submit Tracking Information"):
        if st.session_state.ship_data:
            st.session_state.ship_data[-1]["Start Port"] = start_port
            st.session_state.ship_data[-1]["End Port"] = end_port
            st.session_state.ship_data[-1]["Status"] = tracking_status
            st.success("Tracking information submitted!")
        else:
            st.error("Please enter ship information first.")

elif selected == "Data Visualization":
    st.header("Data Visualization")
    
    if st.session_state.ship_data:
        df = pd.DataFrame(st.session_state.ship_data)

        # Bar chart for tracking status
        status_counts = df['Status'].value_counts()
        fig1 = px.bar(status_counts, x=status_counts.index, y=status_counts.values, 
                      labels={'index': 'Status', 'y': 'Number of Ships'},
                      title="Number of Ships by Status")
        st.plotly_chart(fig1)

        # Pie chart for cargo types
        cargo_counts = df['Type of Cargo'].value_counts()
        fig2 = px.pie(cargo_counts, names=cargo_counts.index, values=cargo_counts.values, 
                      title="Cargo Type Distribution")
        st.plotly_chart(fig2)

    else:
        st.error("No data available for visualization.")
