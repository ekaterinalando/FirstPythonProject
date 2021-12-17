import json

with open('people.json', 'r', encoding='utf8') as file:
        data = json.load(file)



for person in data['people']:
    if not person['has_licence']:
        del person['has_licence']

with open('people_edited.json', 'w', encoding='utf8') as wfile:
    json.dump(data, wfile, indent=2)