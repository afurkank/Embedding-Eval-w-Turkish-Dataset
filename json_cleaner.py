import json

path = "path/to/STS22_tr.json"

# Load the original JSON data
with open(r"path", 'r') as file:
    original_data = json.load(file)

# Create a new dictionary with the desired structure
new_data = {
    "Evaluation Language": "Turkish",
    "Dataset": "STS22",
    "Data": []
}

# Iterate over the original data and add to the new dictionary
for model, scores in original_data.items():
    model_data = {
        "Model": model,
        "Scores": scores
    }
    new_data["Data"].append(model_data)

# Save the new dictionary as a JSON file
with open('benchmark_results.json', 'w') as file:
    json.dump(new_data, file, indent=4)
