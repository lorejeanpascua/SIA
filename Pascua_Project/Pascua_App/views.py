from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pet_list(request):

    pets = Pets.objects.all()

    context = {
        'pets': pets
    }
    return render(request, 'VetcareApp/pet_list.html', context)