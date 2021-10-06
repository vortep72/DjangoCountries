import json
from django.shortcuts import render

with open("country-by-languages.json", "r") as file:
    countries = json.load(file)


def main(request):
    '''return main page'''
    return render(request, 'index.html')


def countries_list_page(request):
    '''return list countries'''
    countries_list_page = {
            'countries': countries
            }
    return render(request, 'countries_list.html', countries_list_page)


def country_page(request, country):
    '''returns each country as a separate page'''
    for line in countries:
        if line['country'] == country:
            country_page = {
                'country': line
            }
            return render(request, 'country.html', country_page)


def languages_list_page(request):
    for language in countries:
        if language['languages']:
            languages_list_page = {'languages': language}
            return render(request, 'languages.html', languages_list_page)
