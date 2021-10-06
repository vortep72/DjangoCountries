import json


with open("country-by-languages.json", "r") as file:
    countries = json.load(file)

countries_list = []
for line in countries:
    country_name = line['country']
    countries_list.append(country_name)


lang_list = []
for country in countries_list:
    for line in countries:
        if country == line['country']:
            lang_list.append({country: line['languages']})


for line in countries:
    if line['country']:
        country_name = line['country']
        countries_list_page = {
            'country': country_name
        }

    if line['country'] == country_name:
        lang_page = {
            'languages': line['languages']
        }
