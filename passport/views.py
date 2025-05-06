from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from passport.models import Country, Passport_type
from passport.forms import PassportFilterForm, CountryForm


def index(request):
    return render(request, 'index.html')

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

def passport_list(request):
    passports = Passport_type.objects.all()
    return render(request, 'passport_list.html',{'passports': passports})

def filter_by_passport(request):
    form = PassportFilterForm(request.GET or None)
    countries = None

    if form.is_valid():
        selected_type = form.cleaned_data['Passport_type']
        countries = Country.objects.filter(Passport_type=selected_type)

    return render(request, 'filter_results.html', {'form': form, 'countries': countries})


def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/passport/countries')  # veya başka bir sayfa
    else:
        form = CountryForm()
    return render(request, 'add_country.html', {'form': form})

def country_comment(request, slug):
    post = get_object_or_404(Country, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        "post": post,
    }
    return render(request, "countries.html", context)
