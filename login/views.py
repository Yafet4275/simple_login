from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.http import HttpResponseRedirect

def login1(request):
    if request.method=='POST':
        #form=ChoreForm(request.POST)
        username = (request.POST['username'])
        print(username)
        password = (request.POST['password'])
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            #return redirect('home')
            return render(request, 'login/home.html')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'login/login.html')
    

def home(request):
    return render(request, 'login/home.html')

"""def home(request):
    username = request.POST['username']
    print(username)
    password = request.POST['password']
    print(password)
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('home')
    else:
        # Return an 'invalid login' error message.
        return redirect('login1')"""
