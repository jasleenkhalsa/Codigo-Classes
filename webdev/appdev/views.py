from django.shortcuts import render,HttpResponse, redirect
from appdev.models import TableOne

def home(request):
    if request.method == 'POST':
        name = request.POST.get('var_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        
        TableOne.objects.create(name = name, mobile=mobile, email = email)
        return redirect('/')

     #   print(f"Name: {name}, Mobile: {mobile}, Email: {email}")
    return render(request, 'home.html')
    



# Create your views here.
