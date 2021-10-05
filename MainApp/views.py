from django.shortcuts import render
import reform_json

# Create your views here.

data = reform_json.country


def main(request):
    return render(request, 'index.html')


def countries(request):
    countries_list = {
        'country': data
    }
    return render(request, 'countries_list.html', countries_list)
