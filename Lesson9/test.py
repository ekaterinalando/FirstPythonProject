import json
json_string =  '''{
    "people": [
      {
        "name": "Jack Sumers",
        "phone": "555-555-555",
        "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
        "has_licence": false,
        "salary": 1500
      },
      {
        "name": "Mary Smith",
        "phone": "777-777-777",
        "emails": null,
        "has_licence": true,
        "salary": 1700
      },
      {
        "name": "Steven Cooke",
        "phone": null,
        "emails": "stevencooke@example.com",
        "has_licence": true,
        "salary": 2500
      }
    ]
  }'''

data = json.loads(json_string)
print(data['people'][0]['has_licence'])

for person in data['people']:
    print(person)

new_json = json.dumps(data, indent=2, sort_keys=True)
print(new_json)