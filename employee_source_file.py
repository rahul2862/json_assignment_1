import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read JSON file
with open('E:\codes\employee.json') as file:
    data = json.load(file)

# Extract employee information from JSON
employee_list = []
for employee_data in data['employees']:
    name = employee_data['Name']
    dob = employee_data['DOB']
    height = employee_data['Height']
    city = employee_data['City']
    state = employee_data['State']
    employee = Employee(name, dob, height, city, state)
    employee_list.append(employee)

# Print the list of Employee objects
for employee in employee_list:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()
_
