from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404,HttpResponseForbidden
from .models import appointment, providers, superUser, users
from .forms import newAppointment, usersForm, superuserForm, loginForm
from datetime import timedelta
from django.template import loader
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from copy import deepcopy
import json
# Create your views here.
HOUR = [
    ('1', '8:00',
     '2', '9:00',
     '3', '10:00',
     '4', '11:00',
     '5', '12:00',
     '6', '13:00',
     '7', '14:00',
     '8', '15:00',)
]

def signup(request):    
    """Logica para poder crear una cuenta
    en base al form, si es correcta se guarda. 
    """
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
    """Funcion crea un usuario administrador si se ingreso
    la frase secreta de forma correcta
    """
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
    """Funcion se encarga del a logica para hacer login y 
    ver si la cuenta que quiere ingresar es admin o no.
    Retorna forbidden si los valores de la cuenta estan mal
    """
    note = '1'
    new_form = loginForm()
    if request.method == 'POST':
        filled_form = loginForm(request.POST)
        if filled_form.is_valid():
            emailInput = filled_form.cleaned_data['email']
            if filled_form.cleaned_data['superUser']:
                #look for superuser accs
                if superUser.objects.filter(email=emailInput, password=filled_form.cleaned_data['password']):
                    print('logged in super')
                    return processLogin(emailInput, request, isSuper= True, logState= True)                   
            else:
                if users.objects.filter(email=emailInput, password=filled_form.cleaned_data['password']):
                    print('logged in normal')
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
    """Si la cuenta esta bien se guarda el email del usuario actual de la sesion
    para obtener informacion luego
    """
    if logState:
        if isSuper:            
            request.session['loggedUser'] = userEmail      
            return redirect('admin/panel/')
        else:             
            request.session['loggedUser'] = userEmail 
            return redirect('user/modify/')                                     
    else: 
        #User got to this url and is not logged in
        return HttpResponseForbidden()

def superuserView(request):     
    return render(request,
                          'superuser_view.html',)

def setDate(request):
    new_form = newAppointment()
    if request.method == 'POST':
       return render(
            request,
            'user_view.html',
            {
                'user_logged': True,
                'dateForm': new_form,
            }
        ) 
    else:
        return render(
            request,
            'user_view.html',
            {
                'user_logged': True,
                'dateForm': new_form,
            }
        )

def userDelete2(request, key):
    """Funcion sabe cual fecha debe borrar 
    con la llave del url
    """
    currentUser = request.session.get('loggedUser')        
    urlNumber = int(key)-1        
    listofAppointments = getUserAppointments(currentUser) 
    dateToDelete = listofAppointments[urlNumber]    
    appointment.objects.get(appointmentDate=dateToDelete).delete()
    return redirect('userDelete')

def userView(request):
    currentUser = request.session.get('loggedUser')
    if currentUser!=None:        
        newform = newAppointment()
        appointmentList = getUserAppointments(currentUser) 
        dateList = [x.date() for x in appointmentList]           
        provider = list(appointment.objects.values_list('provider', flat=True).filter(patient = users.objects.get(email=currentUser).id))
        return render(request,
                            'user_view.html',
                            {
                                'user_logged': True,
                                'datelist' : dateList,
                                'user_name' : currentUser,
                                'providerlist' : provider
                            })
    else:
        return redirect('login')

def userDelete(request):
    """Vista para borrar las citas que tiene
    un usuario 
    """
    currentUser = request.session.get('loggedUser')
    newform = newAppointment()
    appointmentList = getUserAppointments(currentUser)
    #request.session['listofappointments'] = appointmentList 
    formattedList = processAppointmentList(appointmentList)  
    print('at delete')
    provider = list(appointment.objects.values_list('provider', flat=True).filter(patient = users.objects.get(email=currentUser).id))
    return render(request,
                  'user_delete_view.html',
                  {                  
                    'user_logged': True,
                    'datelist' : appointmentList,
                    'user_name' : currentUser,
                  })
    
def userModify(request):
    """View permite crear citas al usuario
    """
    currentUser = request.session.get('loggedUser')    
    newform = newAppointment()
    note = ''
    if request.method == 'POST':        
        filled_form = newAppointment(request.POST)
        if filled_form.is_valid():
            appointmentList = getUserAppointments(currentUser)            
            date = filled_form.cleaned_data['appointmentDate']
            availDates = getAvailableDatesForTheDay(appointmentList, date.day)
            #if len(availDates)!=0:
            try:
                filled_form.save()
            except:
                note = 'Date is already taken, try again or try a different provider'
                return render(request, 'user_Modify_view.html',
                          {
                              'note' : note,
                              'dateForm' : newform,                            
                          })
            print('here3')
            note = 'Saved date for user ' + currentUser + ' date: ' + date.strftime("%m/%d/%Y")
            return render(request, 'user_Modify_view.html',
                          {
                              'note' : note,
                              'dateForm' : newform,
                              'saved' : True,
                          })
        else:
            note = 'Invalid Date Try Again' 
            print('here2')
            return render(request, 'user_Modify_view.html',
                          {
                              'note' : note,
                              'dateForm' : newform,
                          })
    else:    
        print('here')
        return render(request,
                    'user_Modify_view.html',
                    {
                        'note' : note,
                        'dateForm' : newform,
                    })


def availableDatesForProvider(providerName):
    listOfDatesForProvider = appointment.objects.values_list('appointmentDate', flat=True).filter(provider = providerName)
    #parse over dates 
    
    return None

def getAvailableDatesForTheDay(listOfDates, day):
    print(listOfDates)
    print(day)
    for date in listOfDates:
        if date.day == day:
            return [x for x in HOUR if x != date.hour]

def fixUTCTime(datetimeList):
    return [datetime-timedelta(hours=6) for datetime in datetimeList] 

def getUserAppointments(userMail):
    print(users.objects.get(email=userMail).id)
    return appointment.objects.values_list('appointmentDate', flat=True).filter(patient = users.objects.get(email=userMail).id)
    
def deleteAppointment(userMail, dateToDelete):
    appointmentList = getUserAppointments(userMail)
    for date in appointmentList:
        if date == dateToDelete:
            appointment.objects.filter(appointmentDate = dateToDelete).delete()
            
def processAppointmentList(appointmentList):
    return 1    

def new(request):    
    return HttpResponse('Showing \'new\' page')


def show(request, pk=None):
    return HttpResponse('Showing "show" page')

def home(request):
    currentUser = request.session.get('loggedUser')  
    if currentUser!=None:
        return render(request,
                      'home.html',
                      {'user_logged' : True})        
    else:                
        return render(
            request,
            'home.html',
            {}
        )

def about(request):
    return render(
        request,
        'about.html',
        {}
    )

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'