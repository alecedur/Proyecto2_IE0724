from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404,HttpResponseForbidden
from .models import appointment, superUser, users
from .forms import usersForm, superuserForm, loginForm
# Create your views here.

def signup(request):    
    new_form = usersForm()  
    user_logged = False
      
    if request.method == 'POST': 
        filled_form  = usersForm(request.POST)
        # Check valid form 
        user_logged = createUser(filled_form)
        note = ('New User created with email \'{}\''.format(filled_form.cleaned_data['email'])) if user_logged else 'Invalid form, no new user was created...'
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

def createUser(form):
    if form.is_valid(): 
        if form.cleaned_data['key'] == 'SECRET':
            addSuperTrait(form).save()
        else:
            form.save()
        return True 
    else:
        return False
    
def addSuperTrait(form):
    tempForm = form.save(commit=False)
    tempForm.isSuper = True 
    return tempForm

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
    
def login(request):
    note = '1'
    new_form = loginForm()
    if request.method == 'POST':
        filled_form = loginForm(request.POST)
        if filled_form.is_valid():
            emailInput = filled_form.cleaned_data['email']
            if filled_form.cleaned_data['superUser']:
                #look for superuser accs
                if superUser.objects.filter(email=emailInput, password=filled_form.cleaned_data['password']):
                    print('logged in')
                    return processLogin(emailInput, request, isSuper= True, logState= True)                   
            else:
                if users.objects.filter(email=emailInput, password=filled_form.cleaned_data['password']):
                    print('logged in')
                    return processLogin(emailInput, request, logState= True)
            return processLogin(emailInput, request)   
                #look for normal accounts: 
    else:    
        return render(
            request,
            'login_page.html',
            {
                'note' : note,
                'loginForm' : new_form,
            }
        )

def processLogin(userEmail, request, isSuper = False, logState = False):
    if logState:
        if isSuper:
            return redirect('user/view/')
        else:
            return redirect('admin/panel/')               
    else: 
        #User got to this url and is not logged in
        return HttpResponseForbidden()

def superuserView(request):
    return render(request,
                          'superuser_view.html',)
def userView(request):
    return render(request,
                          'user_view.html',)
    

def availableDates(providerName):
    #listOfDatesForProvider = appointment.objects.values_list('appointmentDate', flat=True).filter(provider = providerName)
    #parse over dates 
    return None
    
    

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
