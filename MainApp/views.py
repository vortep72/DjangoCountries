from django.shortcuts import render
import reform_json

# Create your views here.

data = reform_json.countries


def main(request):
    return render(request, 'index.html')


def countries(request):
    countries_list = {
        'countries': data
    }
    return render(request, 'countries_list.html', countries_list)
