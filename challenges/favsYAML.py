#start by importing what i need

import yaml
import json

#Step 1: Import the json file as a file object
file_path = 'favs.json'
yaml_file_path = 'favs.yaml'


 # Open the file in read mode as a file object
with open(file_path, 'r') as file_object:
    # Load the JSON data from the file object
    data = json.load(file_object)

# Now 'data' contains the contents of the JSON file as a Python object (dictionary, list, etc.)
print(data)


#Step 2: Add yourself and your favorites to this list!
# Step 2: Append the new dictionary to the data
new_dict = {
    "name": "marylyn",
    "movie": "Barbie",
    "ice cream": "chocolate chip",
    "color": "forest green",
}

data.append(new_dict)

# Step 2 (contd): Write the updated data back to the JSON file
with open(file_path, 'w') as file_object:
    json.dump(data, file_object, indent=4)

print("New dictionary added to the JSON file.")




# Step 3: Convert the JSON data to YAML and write it to the YAML file
with open(yaml_file_path, 'w') as yaml_file:
    yaml.dump(data, yaml_file, sort_keys=False)
    

print("Data converted to YAML and saved to the YAML file.")



