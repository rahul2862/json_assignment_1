import json

# Create dictionary of Indian states and capitals
states = {
    "Andhra Pradesh": "Hyderabad",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur",
    "Tamil Nadu": "Chennai"
}

# Write the dictionary into a JSON file
with open('states.json', 'w') as file:
    json.dump(states, file)

print("JSON file created successfully.")

