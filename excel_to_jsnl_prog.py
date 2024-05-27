import pandas as pd
import torch
import json
import os

# Load data from Excel file
excel_file_path = 'C:\Users\bbtrust33\OneDrive\Desktop\python_prog'
data = pd.read_excel(excel_file_path)

# Convert data to JSON
data_json = data.to_json(orient='records')

# Create a folder to store the JSON file
json_folder_path = 'json_data'
if not os.path.exists(json_folder_path):
    os.makedirs(json_folder_path)

# Save the JSON file
json_file_path = os.path.join(json_folder_path, 'data.json')
with open(json_file_path, 'w') as f:
    f.write(data_json)

print(f"JSON file saved to {json_file_path}")