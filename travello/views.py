from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = "The City never sleeps"
    dest1.img = 'destination_1.jpg'
    dest1.offer = False
    dest1.price = 2500

    dest2 = Destination()
    dest2.name = 'Ulhasnagar'
    dest2.desc = 'Thane ka nallah'
    dest2.img = 'destination_2.jpg'
    dest2.offer = True
    dest2.price = 1564

    dest3 = Destination()
    dest3.name = 'Worli Gaon'
    dest3.desc = 'Kinny ka ghar'
    dest3.img = 'destination_3.jpg'
    dest3.offer = False
    dest3.price = 3001

    dests = [dest1,dest2,dest3]
    return render(request, 'index.html',{'dests' : dests})

