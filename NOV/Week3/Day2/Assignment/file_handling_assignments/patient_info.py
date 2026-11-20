# Question 10: Hospital Patient Information (JSON)

import json

patient = {
    "patient_id": input("Enter Patient ID: "),
    "name": input("Enter Patient Name: "),
    "age": int(input("Enter Age: ")),
    "disease": input("Enter Disease: "),
    "doctor_name": input("Enter Doctor Name: ")
}

# Write JSON file
with open("patient_info.json", "w") as file:
    json.dump(patient, file, indent=4)

# Read JSON file
with open("patient_info.json", "r") as file:
    data = json.load(file)

print("\nPatient Information")

for key, value in data.items():
    print(key, ":", value)