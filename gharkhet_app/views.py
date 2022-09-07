from django.shortcuts import render
from . models import Gharkhet
# Create your views here.


def home(request):
    gharkhet = Gharkhet.objects.all()
    return render(request, 'gharkhet_app/home.html', {'gharkhet': gharkhet})


def home_detail(request, item):
    ghar = Gharkhet.objects.get(title=item)
    return render(request, 'gharkhet_app/home_detail.html', {'ghar': ghar})
