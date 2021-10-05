from django.shortcuts import render
import reform_json

# Create your views here.

data = reform_json.country


def main(request):
    context = {
        'country': data
    }
    return render(request, 'index.html', context)
