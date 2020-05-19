from django.shortcuts import render
import requests
from .forms import CountryForm

# Create your views here.
def home(request):
    url="https://api.covid19api.com/world/total"
    r=requests.get(url).json()
    worldwide={
        'TotalConfirmed':r['TotalConfirmed'],
        'TotalDeaths':r['TotalDeaths'],
        'TotalRecovered':r['TotalRecovered'],
    }
    
    form=CountryForm()
    country_dict={}
    if request.method=='POST':
        form=CountryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            country_url="https://api.covid19api.com/live/country/{}"
            country_r=requests.get(country_url.format(name)).json()
            country_dict={
                'recovered':country_r[-1]['Recovered'],
                'deaths':country_r[-1]['Deaths'],
                'confirmed':country_r[-1]['Confirmed'],
            }

    context={
        'worldwide':worldwide,
        'form':form, 
        'country_dict':country_dict 
    }
    return render(request,'individual/home.htm', context)
