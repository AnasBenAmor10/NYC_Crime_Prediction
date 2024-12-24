# 🗽 New York City Crimes Detection Using Machine Learning

<div align="center">
  <h4>
    <a href="#overview">📋 Overview</a> |
    <a href="#dataset">📊 Dataset</a> |
    <a href="#notebooks">💻 Notebooks</a> |
    <a href="#technologies">🛠️ Technologies</a> |
    <a href="#install-dependencies">🚀 Install Dependencies </a>|
    <a href="#how-to-run">🚀 How to Run</a>|
    <a href="#user-interface">🖥️ User Interface</a> |
    <a href="#paper">📄 Paper</a>
  </h4>
</div>

---

## 📋 Overview

Predicting crime probabilities is crucial for enhancing public safety. This machine learning-based web application utilizes historical crime data from New York City to provide valuable insights into potential crime occurrences. By integrating user-specific details such as location and time, the application empowers users to make informed decisions and take preventive actions. Whether planning a route, selecting a residential area, or staying aware of potential risks, this tool offers a proactive approach to personal safety.

---

## 📊 Dataset

This project leverages the [NYPD Complaint Data Historic Dataset](https://data.cityofnewyork.us/). The dataset includes all valid felony, misdemeanor, and violation crimes reported to the New York City Police Department (NYPD) from 2006 to 2021. It contains:

- **6,901,167 complaints**  
- **35 columns** of data, including spatial and temporal information, crime descriptions, and penal classifications.

---

## 💻 Notebooks

The repository includes the following Jupyter notebooks:

- 🧹 [**Data Cleaning & Exploratory Data Analysis (EDA)**](research/EDA.ipynb)  
  Perform initial data cleaning and explore key patterns in the dataset.

- 🤖 [**Data Preparation & Modeling**](research/Modeling.ipynb)  
  Train and evaluate machine learning models for crime prediction.

---

## 🛠️ Technologies

### 🌐 Web Application:
- **Streamlit** - for building interactive dashboards  
- **Folium** - for map visualizations  
- **geopy** - for geocoding  
- **geopandas** - for spatial data manipulation  
- **shapely** - for geometric operations  
- **Docker** - for containerization and deployment  

### 📈 Data Cleaning, EDA, and Modeling:
- **Pandas** - data manipulation  
- **seaborn** - statistical visualization  
- **matplotlib** - data plotting  
- **Scikit-learn** - machine learning  
- **LightGBM** - gradient boosting  
- **XGBoost** - gradient boosting  
- **CatBoost** - categorical boosting  

---
## Install Dependencies

It is recommended to use a virtual environment to isolate dependencies. Follow these steps:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. To install the required Python libraries, run:
  ```bash
  cd app
  pip install -r requirements.txt
  ```

---
## 🚀 How to Run

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/your-repo/nyc-crime-detection.git
   cd NYC_Crime_Prediction
   ```

2. **Start the Application**:  
   Use Streamlit to launch the application locally:
   ```bash
   cd app
   streamlit run main.py
   ```

3. **Access the Application**:  
   Open your web browser and navigate to:  
   ```
   http://localhost:8501
   ```

4. **Interact with the Tool**:  
   - Select a location on the map.
   - Provide your details in the form.
   - View the crime predictions.


## 🖥️ User Interface

Below are examples of the application's user interface:  

📍 **Interface**  
<img src="Images/Interface.PNG" alt="User Interface Example 1" width="600">

📈 **Map Visualization & Prediction Results**  
<img src="Images/Selected_position.PNG" alt="User Interface Example 2" width="600">
<img src="Images/Form.PNG" alt="User Interface Example 2" width="600">



---

## 📄 Paper

Our research findings are documented in a paper included in this repository. You can view the paper [here](docs/NYC_Paper.pdf).

---

## 🙌 Credits

This project was built by the team:

- **Nour Mabrouk**  
- **Bacem Ahmed**  
- **Anas Ben Amor** 
