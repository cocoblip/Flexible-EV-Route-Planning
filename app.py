"""
Flask web app for route planning and map generation.
Provides endpoints to render the home page and generate routes.
"""
from flask import Flask, request, jsonify, render_template
import os
import map_construction

# Initialize Flask app
app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    # Home page endpoint
    return render_template("index.html")

@app.route("/generate-route", methods=["POST"])
def generate_route():
    # Route planning endpoint
    try:
        # parse input parameters from the submitted form
        start = request.form["start"]
        destination = request.form["destination"]
        initial_soc = float(request.form["initial_soc"])
        threshold_soc = float(request.form["threshold_soc"])
        consumption_rate = float(request.form["consumption_rate"])
        
        # execute the route planning function
        road_network, charging_stations, paths, costs, map_filename_or_status, legend_html = map_construction.test_route_planning(
            start, destination, initial_soc, threshold_soc, consumption_rate
        )

        if map_filename_or_status == "invalid_address":
            return jsonify({"success": False, "error": "Invalid address entered. Please check your start or destination address."})

        expected_map_filename = map_filename_or_status
        
        if paths is None:
            return jsonify({"success": False, "error": "No valid paths found."})

        os.makedirs("static/maps", exist_ok=True)
        
        static_map_path = f"static/maps/route_{start.replace(' ', '_')}_{destination.replace(' ', '_')}.html"
        
        if os.path.exists(expected_map_filename):
            import shutil
            shutil.copy(expected_map_filename, static_map_path)
        else:
            return jsonify({"success": False, "error": f"Map file {expected_map_filename} was not generated."})

        return jsonify({"success": True, "map_url": "/" + static_map_path, "legend_html": legend_html})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    # Run the Flask development server with debug mode on
    app.run(debug=True)

