# Flexible EV Route Planning: Balancing Travel Time and Charging Station Proximity
### _Contributors: Zi Hao Li, Palkan Motwani_

This project implements an advanced route planning system for electric vehicles (EVs) that optimizes both travel time and charging safety proximity. The system processes road network data from British Columbia, calculates distances to nearest charging stations, and renders the optimal routes on interactive maps. This tool helps EV drivers plan journeys with confidence, addressing range anxiety by providing routes that balance efficiency with charging accessibility.

## 1. Features

- Multi-Objective Optimization: Balances travel time and charging safety concerns
- Pareto-Optimal Paths: Generates non-dominated solutions representing different trade-offs
- Battery Constraints: Ensures routes maintain sufficient battery charge throughout the journey
- Real Road Network: Uses OpenStreetMap data for realistic route planning
- Charging Station Integration: Incorporates real-world charging station locations
- Customizable Parameters: Adjustable initial state of charge, threshold, and energy consumption

## 2. Files Overview
#### 2.1 Data Collection and Processing
- [get_charging_stations.py] - Retrieves EV charging station data for BC regions and saves to charging_stations_bc_regions.json. 
🚀 Estimated runtime is 30 sec 🚀
- [get_road_networks.py] - Downloads road network data from OpenStreetMap for BC regions and saves to roads_bc_regions.json.
✅  Estimated runtime  is 2 min  ✅ 
- [calculate_nearest_stations.py] - Calculates the nearest charging station for each road network node, computing actual road distances rather than straight-line distances. Results are saved to intersections_bc_regions.json.
⚠️ Estimated runtime is 30 hr ⚠️

#### 2.2 Route Planning and Visualization
- [map_construction.py] - Implements Multi-Objective A algorithm to find optimal routes balancing travel time and charging safety. Reads road network, charging stations, and pre-calculated nearest station data. When an electric vehicle requires mid-trip charging, the journey is divided into two segments. A suitable charging station is selected as the endpoint of the first segment and the starting point of the second segment.
- [map_renderer.py] - Visualizes generated routes on interactive maps using Folium, highlighting paths and showing charging stations.

#### 2.3 Web Application
- [app.py] - Flask web server that provides an API for the route planning functionality. Handles user requests, processes route planning parameters, executes the planning algorithm, and serves the generated route visualizations.
- [index.html] in templates folder - Frontend interface that allows users to input route parameters (start/end locations, battery settings) through a user-friendly web form. Communicates with the Flask backend and displays the resulting route maps.

#### 2.4 Generated Data Files (3 json files are shared on google drive)
You can directly download it, which will save you 30 hours of code runtime.
https://drive.google.com/drive/folders/1tJ-hupmy-jRwhjazsb-d11Hny7CGkxss?usp=drive_link
- [charging_stations_bc_regions.json] - Contains charging station locations and details.
- [roads_bc_regions.json] - Contains road network graph with nodes (intersections) and edges (road segments).
- [intersections_bc_regions.json] - Contains pre-calculated data mapping each intersection to its nearest charging station.
- [pareto_paths_[start]_[end].html] - Interactive map visualization showing the Pareto-optimal routes between specified start and end points. Generated after running the route planning algorithm.


## 3. Installation
To run this project, you need Python 3.7+ and the following dependencies:
#### 3.1 Core dependencies:
These packages are required for the core functionality of the EV Route Planner:
| Dependencies | Functionalities |
| ------ | ------ |
| requests | For API requests |
|json|For JSON processing (part of Python standard library)|
|folium|For interactive map visualization|
|osmnx|For working with OpenStreetMap data|
|networkx|For graph operations and algorithms|
|math|For mathematical operations (part of Python standard library)|
|shapely|For geometric operations|
|queue|For priority queue implementation (part of Python standard library)|
|re|For regular expressions (part of Python standard library)|
|flask| For web framework support |

#### 3.2 Additional dependencies
These packages enhance functionality or improve performance:
| Dependencies | Functionalities |
| ------ | ------ |
|matplotlib | For plotting |
|numpy | For numerical operations|
|pandas | For data manipulation|
|geopandas | For geospatial data operations|
|rtree | For spatial indexing |

## 4. Steps to Operate
1. Download all the files and save them in the same directory.
2. pip install -r requirements.txt to install dependencies
3. Run the `app.py` file.  
4. Copy and paste the generated URL into your browser.  
5. Enter the starting point, destination, and other custom parameters in the input fields. Please choose 2 addresses in the Create Vancouver or Fort St. John.

   **Note**: If the address you enter includes a specific street number, the generated map's start and end points may be slightly different from your input. This is because we select the nodes closest to the input address as the start and end points.
7. Click the **Generate Route** button.  
8. Wait for the visualized map to be generated.

   **Note**: The first time the map is generated, it takes longer than subsequent times because the program needs to load the map and road network data.

## 5. How can our application be adapted for use with different geographic regions?
1. The default setting involves selecting a rectangular area as the region of interest. First, obtain the latitude and longitude coordinates of the four boundaries defining the rectangular region. Then, place thses four values into a list in the order of [Southern latitude boundary, Western longitude boundary, Northern latitude boundary, Eastern longitude boundary].
2. Update the code defining the rectangular area boundaries in the generate_charging_stations_data() function within get_charging_stations.py; update the filename of the generated JSON file accordingly.
3. Update the code defining the rectangular area boundaries in the generate_roads_data() function within get_road_networks.py; update the filename of the generated JSON file accordingly.
4. Execute the updated get_charging_stations.py and get_road_networks.py scripts with an active internet connection.
5. Execute calculate_nearest_stations.py script with two new json files.
6. Repeat step 2 to 8 in **Steps to Operate**
