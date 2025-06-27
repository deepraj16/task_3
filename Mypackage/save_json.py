import json

json_file = "score.json"
def save_score(name, score):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[name] = score

    with open(json_file, 'w') as file:
        json.dump(data, file)

    print(f"Score for {name} saved successfully.")
