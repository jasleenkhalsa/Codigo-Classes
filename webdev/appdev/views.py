from django.shortcuts import render,HttpResponse, redirect
from appdev.models import TableOne

def home(request):
    user_data = TableOne.objects.all()

    if request.method == 'POST':
        name = request.POST.get('var_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        file = request.FILES.get('file')

        TableOne.objects.create(name = name, mobile=mobile, email = email, file = file)
        return redirect('/')
    # json -> {dict}
    # data_front = {
      #   'data': user_data}
    

     #   print(f"Name: {name}, Mobile: {mobile}, Email: {email}")
    return render(request, 'home.html', {'data' : user_data})
    

'''
data
'''
