import json

path = "path/to/benchmark/results"

# Load the JSON data from the file
with open(r"path") as file:
    data = json.load(file)

max_score = float('-inf')
max_model = None

# Iterate over the data items
for item in data['Data']:
    model = item['Model']
    scores = item['Scores']
    cos_sim_pearson = scores['cos_sim']['pearson']

    # Check if current score is higher than the maximum score
    if cos_sim_pearson > max_score:
        max_score = cos_sim_pearson
        max_model = model

print(f"The model with the highest cos_sim-pearson score is: {max_model}")
print(f"The highest cos_sim-pearson score is: {max_score}")

max_score = float('-inf')
max_model = None
# Iterate over the data items
for item in data['Data']:
    model = item['Model']
    scores = item['Scores']
    cos_sim_spearman = scores['cos_sim']['spearman']
    
    # Check if current score is higher than the maximum score
    if cos_sim_spearman > max_score:
        max_score = cos_sim_spearman
        max_model = model

print(f"The model with the highest cos_sim_spearman score is: {max_model}")
print(f"The highest cos_sim_spearman score is: {max_score}")

max_score = float('-inf')
max_model = None
# Iterate over the data items
for item in data['Data']:
    model = item['Model']
    scores = item['Scores']
    euclidean_pearson = scores['euclidean']['pearson']
    
    # Check if current score is higher than the maximum score
    if euclidean_pearson > max_score:
        max_score = euclidean_pearson
        max_model = model

print(f"The model with the highest euclidean_pearson score is: {max_model}")
print(f"The highest euclidean_pearson score is: {max_score}")

max_score = float('-inf')
max_model = None
# Iterate over the data items
for item in data['Data']:
    model = item['Model']
    scores = item['Scores']
    euclidean_spearman = scores['euclidean']['spearman']
    
    # Check if current score is higher than the maximum score
    if euclidean_spearman > max_score:
        max_score = euclidean_spearman
        max_model = model

print(f"The model with the highest euclidean_spearman score is: {max_model}")
print(f"The highest euclidean_spearman score is: {max_score}")

max_score = float('-inf')
max_model = None
# Iterate over the data items
for item in data['Data']:
    model = item['Model']
    scores = item['Scores']
    manhattan_pearson = scores['manhattan']['pearson']
    
    # Check if current score is higher than the maximum score
    if manhattan_pearson > max_score:
        max_score = manhattan_pearson
        max_model = model

print(f"The model with the highest manhattan_pearson score is: {max_model}")
print(f"The highest manhattan_pearson score is: {max_score}")

max_score = float('-inf')
max_model = None
# Iterate over the data items
for item in data['Data']:
    model = item['Model']
    scores = item['Scores']
    manhattan_spearman = scores['manhattan']['spearman']
    
    # Check if current score is higher than the maximum score
    if manhattan_spearman > max_score:
        max_score = manhattan_spearman
        max_model = model

print(f"The model with the highest manhattan_spearman score is: {max_model}")
print(f"The highest manhattan_spearman score is: {max_score}")


best_model = None
best_score = float('-inf')

# Iterate over the data items
for item in data['Data']:
    model = item['Model']
    scores = item['Scores']
    
    # Calculate aggregate score as the average of all individual scores
    aggregate_score = sum(scores[key]['pearson'] + scores[key]['spearman'] for key in scores) / (2 * len(scores))
    
    # Check if current aggregate score is higher than the best score
    if aggregate_score > best_score:
        best_score = aggregate_score
        best_model = model

print(f"The model with the best score among all criteria is: {best_model}")
print(f"The best score is: {best_score}")
