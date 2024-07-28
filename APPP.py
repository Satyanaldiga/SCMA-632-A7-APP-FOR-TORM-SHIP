import streamlit as st

# Title of the app
st.title("TORM Shipping Company - Ship Tracker")

# Sidebar for input
st.sidebar.title("Ship Information")

# Input fields
ship_name = st.sidebar.text_input("Ship Name")
imo_number = st.sidebar.text_input("IMO Number")
mmsi_number = st.sidebar.text_input("MMSI Number")
cargo_type = st.sidebar.selectbox("Type of Cargo", ["Oil", "Gas", "Bulk", "Container", "Other"])
ship_speed = st.sidebar.number_input("Speed of Ship (knots)", min_value=0, max_value=100, value=0)
crew_members = st.sidebar.number_input("Number of Crew Members", min_value=0, max_value=1000, value=0)

# Tracking information
start_port = st.text_input("Start Port")
end_port = st.text_input("End Port")
tracking_status = st.selectbox("Tracking Status", ["In Port", "At Sea", "Arrived"])

# Displaying the entered information
st.subheader("Entered Ship Information")
st.write(f"**Ship Name:** {ship_name}")
st.write(f"**IMO Number:** {imo_number}")
st.write(f"**MMSI Number:** {mmsi_number}")
st.write(f"**Type of Cargo:** {cargo_type}")
st.write(f"**Speed of Ship:** {ship_speed} knots")
st.write(f"**Number of Crew Members:** {crew_members}")

st.subheader("Tracking Information")
st.write(f"**Start Port:** {start_port}")
st.write(f"**End Port:** {end_port}")
st.write(f"**Tracking Status:** {tracking_status}")

# Optionally, you can add more functionality like database connection, real-time tracking, etc.

