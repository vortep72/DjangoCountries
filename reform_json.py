import json
country = []
with open("country-by-languages.json", "r") as file:
    for line in json.load(file):
        k = 'country'
        d = line['country']
        country.append({k: d})
