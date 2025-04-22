from django.shortcuts import render
from django.http import HttpResponse
from passport.models import Country, Passport_type
from passport.forms import PassportFilterForm


def index(request):
    return render(request, 'home.html')

def exchange(request):
    return HttpResponse('kurs verisi')

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})



def passport_list(request):
    passports = Passport_type.objects.all()
    return render(request, 'passport_list.html',{'passports': passports})

def forum(request):
    return render(request, 'forum.html')

def filter_by_passport(request):
    form = PassportFilterForm(request.GET or None)
    countries = None

    if form.is_valid():
        selected_type = form.cleaned_data['Passport_type']
        countries = Country.objects.filter(Passport_type=selected_type)

    return render(request, 'filter_results.html', {'form': form, 'countries': countries})

