from django.shortcuts import render
from django.http import HttpResponse, Http404

#from .models import Pet
#from .forms import PetForm

# Create your views here.


def new(request):
    # new_form = PetForm()

    # if request.method == 'POST':
    #     filled_form = PetForm(request.POST)

    #     # Only save an object from a valid form
    #     if filled_form.is_valid():
    #         new_pet = filled_form.save()
    #         new_pk = new_pet.pk
    #         note = (
    #             'New Pet object with pk \'{}\' was created\n'
    #             'Name: {}'.format(
    #                 new_pk,
    #                 filled_form.cleaned_data['name']
    #             )
    #         )
    #     else:
    #         note = 'Invalid form, no Pet object was created...'

    #     return render(
    #         request,
    #         'new.html',
    #         {
    #             'note': note,
    #             'petform': new_form,
    #         }
    #     )
    # else:
    #     return render(
    #         request,
    #         'new.html',
    #         {
    #             'petform': new_form,
    #         }
    #     )
    return HttpResponse('Showing \'new\' page')


def show(request, pk=None):
    return HttpResponse('Showing "show" page')
