from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

#from django.contrib.auth.views import authenticate


def logout_user(request):
    ''' A view to logout user '''
    logout(request)
    return HttpResponseRedirect(reverse('learninglog:home'))
# Create your views here.

def sign_up(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learninglog:home'))
        else:
            return HttpResponse("The Data you entered is invalid")
    context = {'form':form}
    return render(request,'users/sign_up.html', context )
