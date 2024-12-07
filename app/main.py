import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from datetime import datetime
import service as service
import geopandas as gpd
from shapely.geometry import Point
from pyproj import Proj, transform
import requests

def get_coordinates(destination):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": destination,
        "format": "json",
        "limit": 1,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            return lat, lon
        else:
            print("Location not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_pos(lat, lng):
    return lat, lng

def lon_lat_to_utm(lon, lat):
    utm_proj = Proj(init="epsg:2263")
    utm_x, utm_y = transform(Proj(init="epsg:4326"), utm_proj, lon, lat)
    return utm_x, utm_y

shapefile = './shapes/geo_export_84578745-538d-401a-9cb5-34022c705879.shp'
borough_sh = './borough/nybb.shp'

def get_precinct_and_borough(lat, lon):
    precinct_gdf = gpd.read_file(shapefile)
    borough_gdf = gpd.read_file(borough_sh)
    point = Point(lon, lat)
    point2 = Point(lon_lat_to_utm(lon, lat))
    precinct = None
    borough = None
    for _, row in precinct_gdf.iterrows():
        if row['geometry'].contains(point):
            precinct = row['precinct']
    for _, row in borough_gdf.iterrows():
        if row['geometry'].contains(point2):
            borough = row['BoroName']
            break
    return precinct, borough

def generate_base_map(default_location=[40.704467, -73.892246], default_zoom_start=11, min_zoom=11, max_zoom=15):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start,
                          min_zoom=min_zoom, max_zoom=max_zoom, max_bounds=True, min_lat=40.47739894,
                          min_lon=-74.25909008, max_lat=40.91617849, max_lon=-73.70018092)
    return base_map

def get_user_information():
    """Function to collect all user information within a form"""
    with st.form(key='user_info_form'):
        st.header("Enter your information 📋")

        # Collecting gender with radio buttons
        gender = st.radio("Gender 👤", ["Male", "Female"])

        # Collecting race with a selectbox
        race = st.selectbox("Race 🌍", ['WHITE', 'WHITE HISPANIC', 'BLACK', 'ASIAN / PACIFIC ISLANDER', 
                                       'BLACK HISPANIC', 'AMERICAN INDIAN/ALASKAN NATIVE', 'OTHER'])

        # Collecting age with a slider
        age = st.slider("Age 🧑‍🦳:", 0, 120)

        # Collecting date using date input
        date = st.date_input("Date 🗓️:", datetime.now())

        # Collecting time using time input widget
        time = st.time_input("Hour 🕒:", datetime.now().time())

        # You can then extract the hour from the time object if needed
        hour = time.hour
        # Collecting place with radio buttons
        place = st.radio("Place 📍", ("In park", "In public housing", "In station"))

        # Submit button for the form
        submit_button = st.form_submit_button("Submit 📝")
    
    return gender, race, age, date, hour, place, submit_button

# Streamlit page config
st.set_page_config(
    page_title="NYC Crime Prediction 🚔",
    page_icon="🌍",
    layout="wide",  
    initial_sidebar_state="expanded",  # Sidebar will always be visible (expanded)
)

# Sidebar for additional input options or instructions
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/New_York_City_Skyline_Illustration.jpg/800px-New_York_City_Skyline_Illustration.jpg?20220523133854", use_container_width=True)  # Updated image
    st.markdown("# NYC Crime Prediction")
    st.markdown("""
        This tool helps you predict the likelihood of a crime happening in specific areas of **New York City** based on your demographics and location.
    """)

# Main content area
with st.container():
    st.title("🗽 New York Crime Prediction 🚔🌆")

    # Application description centered with icons
    st.markdown("""
        This tool leverages machine learning models to predict the likelihood of a crime occurring at a specific location in **New York City**. Whether you're planning a visit to NYC or are simply curious about the safety of certain areas, this app helps you understand potential risks based on various factors, such as:

        - **👤 Demographics**: Age, gender, and race—factors that can influence crime trends.
        - **⏰ Time**: The specific day and hour you plan to be out in the city.
        - **📍 Location**: Whether you're in a park, public housing, or a station.

        ### 🔍 How it Works:
        1. **Select your destination** 📍: Choose the area you're interested in via the interactive map.
        2. **Enter your details** 📝: Provide your age, gender, race, and other relevant information.
        3. **Get predictions** 🛑: Based on the provided data, the app will predict the most likely types of crimes you could encounter.

        ### 🚨 Stay Safe and Informed! 🚔🌆
        This tool is designed to keep you informed and help you stay safe while navigating the city. 🌍
    """)

# Render the map **outside the form**
base_map = generate_base_map()
base_map.add_child(folium.LatLngPopup())

# Add a marker with popup for when the user clicks on the map
map = st_folium(base_map, height=350, width=700)

# Instruction to click on the map
st.markdown("""
    **🔑 Click on the map to select your location!** 📍
    After selecting a location, fill in the form below to get a prediction about the crime risks in the area.
""")

# When a location is clicked, get coordinates and display info creatively
if map['last_clicked']:
    lat = map['last_clicked']['lat']
    lon = map['last_clicked']['lng']

    # Get precinct and borough from the selected coordinates
    precinct, borough = get_precinct_and_borough(lat, lon)

    if borough:
        # Create a dynamic popup for coordinates and additional info
        popup_content = f"""
        <b>📍 Selected Coordinates:</b><br>
        <i>Latitude:</i> {lat}<br>
        <i>Longitude:</i> {lon}<br><br>
        <b>Precinct:</b> {precinct} <br>
        <b>Borough:</b> {borough} 🏙️
        """
        
        # Add marker to the map with the popup
        folium.Marker([lat, lon], popup=folium.Popup(popup_content, max_width=300)).add_to(base_map)

        # Display the updated map with marker and popup
        st_folium(base_map, height=350, width=700)

        # Collect user information after selecting location
        gender, race, age, date, hour, place, submit_button = get_user_information()

        # Trigger the crime prediction once the location is confirmed and the form is submitted
        if submit_button:
            # Check for necessary inputs before prediction
            if lat == '' or lon == '' or precinct is None:
                st.error("Please make sure that you selected a location on the map 📍")
            else:
                # Call service to create a DataFrame and predict
                X = service.create_df(date, hour, lat, lon, place, age, race, gender, precinct, borough)
                pred, crimes = service.predict(X)  # Predict after inputs are given
                
                # Display the result with a creative touch
                st.markdown(f"⚠️ Based on your inputs, there's a high likelihood that you could fall victim to a **{pred}** crime. Please stay vigilant and take necessary precautions! 🚨")
    else:
        st.error("Select a destination in NYC 🏙️")
