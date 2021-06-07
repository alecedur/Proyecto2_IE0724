from django.shortcuts import render
from django.http import HttpResponse, Http404

#from .models import Pet
#from .forms import PetForm
from .models import users
from .forms import usersForm, superuserForm
# Create your views here.

def signup(request):    
    new_form = usersForm()  
    user_logged = False
      
    if request.method == 'POST': 
        filled_form  = usersForm(request.POST)
        # Check valid form 
        if filled_form.is_valid():
            print("invalid")
            user_logged = True
            new_user = filled_form.save()
            note = ( 
                    'New User created with email \'{}\''.format(filled_form.cleaned_data['email'])
                    )
        else:
            note = 'Invalid form, no new user was created...'
        
        return render(
            request, 
            'signup.html',
            {
                'note' : note,
                'userform' : new_form,
                'user_logged' : user_logged,
            }            
        )
    else:
        return render(
            request,
            'signup.html',
            {
                'userform' : new_form,
            }
        )

def superuser(request):
    new_form = superuserForm()
    user_logged = False 
    if request.method == 'POST':
        print('post')
        filled_form  = superuserForm(request.POST)
        if filled_form.is_valid() and filled_form.cleaned_data['key'] == 'SECRET':
            user_logged = True
            filled_form.save()
            note = ('New SuperUser created with email \'{}\''.format(filled_form.cleaned_data['email']))            
        else:
            note = 'Invalid form, no new superuser was created...'
        return render(
            request,
            'superuser.html',
            {
                'note' : note, 
                'superuserform' : new_form,
                'user_logged' : user_logged,
            }
        )
        
    else:         
        return render(
            request,
            'superuser.html',
            {
                'superuserform' : new_form,
            }
        )
    

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
