### README
---

# Project Title: Analysis of Demographic and Transportation Data in French Regions

## Overview
This project involves analyzing and visualizing demographic and transportation data for three French regions: Aix-Marseille, Île-de-France, and Grand Lyon. The main aim is to compute commercial kilometers and compare various demographic and transportation metrics across these regions.

## Data Description
The dataset contains various indicators for each region, including:
- **Population:** Total number of inhabitants.
- **Surface (km²):** Total surface area in square kilometers.
- **Density (people/km²):** Population divided by surface area.
- **Commercial kilometers (km²):** Sum of distances covered by commercial lines in kilometers.
- **Commercial kilometers per inhabitant:** Commercial kilometers divided by population.
- **Number of cars:** Total number of cars.
- **Volume of cars per inhabitant:** Number of cars divided by population.

## Prerequisites
- Python 3.7+
- Required Python packages:
  - pandas
  - shapely
  - pyproj
  - geopandas
  - matplotlib (optional, for visualization)
  - IPython (optional, for displaying DataFrame in Jupyter Notebook)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required packages using pip:
    ```bash
    pip install pandas shapely pyproj geopandas matplotlib ipython
    ```

## Usage

### 1. Create Demographic DataFrame
```python
import pandas as pd

# Provided demographic and transportation data
data = { 
    'Indicator': [
        'Population', 'Surface (km²)', 'Density (people/km²)', 
        'Commercial kilometers (km²)', 'Commercial kilometers per inhabitant', 
        'Number of cars', 'Volume of cars per inhabitant'
    ],
    'Aix-Marseille': [1831500, 3173, 1831500 / 3173, 482, 482 / 1831500, 1265189, 1265189 / 1831500],
    'Île-de-France': [12278210, 12012, 12278210 / 12012, 2194, 2194 / 12278210, 4600000, 4600000 / 12278210],
    'Grand Lyon': [1400000, 538, 1400000 / 538, 1405, 1405 / 1400000, 600000, 600000 / 1400000]
}

# Create Pandas DataFrame
df_demographics = pd.DataFrame(data)

# Set display options for better readability
pd.set_option('display.float_format', '{:.6f}'.format)

# Display the created DataFrame
print(df_demographics)

# Display the total number of rows in the DataFrame
print(f"Total rows in DataFrame: {df_demographics.shape[0]}")

# For Jupyter Notebook
from IPython.display import display, HTML

display(HTML(df_demographics.to_html()))
```

### 2. Random Sampling and Commercial Kilometers Calculation
```python
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
import pyproj
from shapely.ops import transform

# Example DataFrames for the regions (replace with actual data)
df_idf = pd.DataFrame({
    "shape_id": ["IDFM:C00029"] * 50,
    "Latitude": [48.804194, 48.798378, 48.794167, 48.79279, 48.790468] * 10,
    "Longitude": [2.60136, 2.605053, 2.604445, 2.604183, 2.603874] * 10
})

df_lyon = pd.DataFrame({
    "shape_id": ["lbl_libellule.lblligne.4747"] * 200,
    "Latitude": [45.980442, 45.98046, 45.98048, 45.9805, 45.98052] * 40,
    "Longitude": [4.700001, 4.70012, 4.70028, 4.70045, 4.70063] * 40
})

df_am = pd.DataFrame({
    "shape_id": ["010161"] * 300,
    "Latitude": [43.295624, 43.295509, 43.29554, 43.295551, 43.295528] * 60,
    "Longitude": [5.56508


API Overview:

This Flask application provides a simple API to serve the sampled data of three metropolitan areas: Aix-Marseille, Grand Paris, and Grand Lyon. Each region has a dedicated route that renders a web page displaying a list of data points.

API Endpoints:
/am - Displays the sampled data for Aix-Marseille.
/paris - Displays the sampled data for Grand Paris.
/lyon - Displays the sampled data for Grand Lyon.

Open your browser and navigate to the following URLs to access the data:
http://127.0.0.1:5000/am
http://127.0.0.1:5000/paris
http://127.0.0.1:5000/lyon
