from django.shortcuts import render
from django.http import HttpResponse
from .forms import loginForm
# Create your views here.

def login_action(request):
    global email, password
    if request.method == 'POST':
        d=request.POST
        for key,value in d.items():
            if key == 'email':
                email = value
            if key == 'password':
                password = value
        form = loginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Saved')
        else:
            return HttpResponse('Data Not Saved')
    else:
        form = loginForm()
    return render(request, 'myapp/login.html', {'form': form})


#age["sachin"] = 45
#age["rahul"] = 50
#age["sachin"] = 55
#age["naman"] = 22
#age = {"sachin":55, "rahul":50, "naman": 1234567890, "dev": "mumbai"}
#key:value
#d = {"email": "abc@gmail.com", "password": "123"}