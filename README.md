# TORM Shipping Company - Ship Tracker

This is a Streamlit application for tracking ships of the TORM Shipping Company. The app allows users to input ship information, track ships from one port to another, and visualize ship data using various charts.

## Features

- **Ship Information**: Input details about ships, including name, IMO number, MMSI number, type of cargo, speed, and number of crew members.
- **Tracking Information**: Enter and display tracking information for ships, such as start port, end port, and current status.
- **Data Visualization**: Visualize ship data with bar charts and pie charts to display the distribution of ship statuses and cargo types.
- **Search Functionality**: Search for a ship by name to view its tracking information.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ship-tracker.git
    cd ship-tracker
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run ship_tracker.py
    ```

## Dependencies

- `streamlit`: A framework for creating interactive web applications.
- `streamlit-option-menu`: A library for creating option menus in Streamlit.
- `plotly`: A graphing library for creating interactive visualizations.
- `pandas`: A data manipulation library for handling ship data.

## Usage

### Ship Information

1. **Navigate to the "Ship Information" tab**.
2. **Input the ship's details**:
    - Ship Name
    - IMO Number
    - MMSI Number
    - Type of Cargo (Oil, Gas, Bulk, Container, Other)
    - Speed of Ship (knots)
    - Number of Crew Members
3. **Submit the information** by clicking the "Submit Ship Information" button.
4. **View the entered ship information** below the input form.

### Tracking Information

1. **Navigate to the "Tracking Information" tab**.
2. **Search for a ship by name** using the text input.
3. **View the tracking information** if the ship is found:
    - Start Port
    - End Port
    - Tracking Status (In Port, At Sea, Arrived)
4. **Enter tracking information** for the last submitted ship:
    - Start Port
    - End Port
    - Tracking Status
5. **Submit the tracking information** by clicking the "Submit Tracking Information" button.

### Data Visualization

1. **Navigate to the "Data Visualization" tab**.
2. **View the bar chart** displaying the number of ships by their tracking status.
3. **View the pie chart** displaying the distribution of cargo types among the ships.

## Custom CSS

The application includes custom CSS to enhance the user interface, including custom styles for the background, buttons, and hover effects.


