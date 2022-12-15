import os
import pickle
import json
import numpy as np

# Path to the directory containing the pickle files
directory = "C:/Users/Nathan/Documents/GitHub/CapstoneWifiAnalysis/Data Processing/SavedPredictions/"

# Loop through every file in the directory
for filename in os.listdir(directory):
    # Check if the file is a pickle file
    if filename.endswith(".pkl"):
        # Construct the full path to the file
        filepath = os.path.join(directory, filename)
        # Read and deserialize the pickle file
        with open(filepath, "rb") as f:
            data = pickle.load(f)

        # Check if the data is a NumPy array
        if isinstance(data, np.ndarray):
            # Convert the NumPy array to a Python list
            data = data.tolist()

        # Serialize the data and write it to a JSON file with the same name
        # as the original pickle file, but with a .json extension
        json_filename = os.path.splitext(filename)[0] + ".json"
        json_filepath = os.path.join(directory, json_filename)
        with open(json_filepath, "w") as f:
            json.dump(data, f)
