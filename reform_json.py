import json
countries = []
with open("country-by-languages.json", "r") as file:
    for line in json.load(file):
        country_name = line['country']
        countries.append(country_name)
