from django.shortcuts import render,redirect
from .forms import *
# Create your views here.



# this function add new item and show in the page
def add_your_data(request):
    form = StudentRegistration()
    student = User.objects.all()
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            register = User(name=name,email=email,password=password)
            register.save()

        return redirect('/')
    context = {'form':form, 'stud':student}
    return render(request,'enroll/data.html',context)





# this is function delete your data
#     
def delete_data(request,id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        data.delete()
    return redirect('/')



# this function should take update your data

def update_data(request,id):
    task = User.objects.get(pk=id)
    form = StudentRegistration(instance=task)

    if request.method == "POST":
        form = StudentRegistration(request.POST, instance=task)
        if form.is_valid():
           form.save()
        return redirect('/')
    
    context = {'form':form}

    return render(request,'enroll/update.html',context)
