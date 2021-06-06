from django.shortcuts import render

# Create your views here.

from django.http.response import Http404, HttpResponse
from .models import Pet

def new(request):
    return HttpResponse('Showing \'new\' page')

def show(request, pk=None):
    if pk is not None:
        try:
            #Query by pk
            pet = Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404('Pet with pk{} doesnt exist'.format(pk))
        return render(
            request,
            'show.html',
            {
                'object_pk': pet.pk,
                'object_name': pet.name,
                'object_age': pet.age,
            }
        )
    else:
        pet_dict = {}
        for pet in Pet.objects.all():
            pet_dict[pet.name] = {
                'pk' : pet.pk,
                'age' : pet.age,
            }   
        # el renderizador agarra el html rellena el codigo dentro y lo va a mostrar
        return render(
            request,
            'show.html',
            {
                'pet_dict': pet_dict,
            }
        )
