from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Pet
from .forms import PetForm

# Create your views here.


def new(request):
    new_form = PetForm()

    if request.method == 'POST':
        filled_form = PetForm(request.POST)

        # Only save an object from a valid form
        if filled_form.is_valid():
            new_pet = filled_form.save()
            new_pk = new_pet.pk
            note = (
                'New Pet object with pk \'{}\' was created\n'
                'Name: {}'.format(
                    new_pk,
                    filled_form.cleaned_data['name']
                )
            )
        else:
            note = 'Invalid form, no Pet object was created...'

        return render(
            request,
            'new.html',
            {
                'note': note,
                'petform': new_form,
            }
        )
    else:
        return render(
            request,
            'new.html',
            {
                'petform': new_form,
            }
        )
    # return HttpResponse('Showing \'new\' page')


def show(request, pk=None):
    if pk is not None:
        try:
            # Query by pk
            pet = Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404('Pet with pk {} doesn\'t exist'.format(pk))

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
                'pk': pet.pk,
                'age': pet.age,
                'gender': pet.gender,
            }

        # pet_dict = {
        #     pet.name: {
        #         'pk': pet.pk,
        #         'age': pet.age,
        #     }
        # }

        return render(
            request,
            'show.html',
            {
                'pet_dict': pet_dict,
            }
        )
