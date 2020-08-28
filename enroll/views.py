from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegister
from django.contrib import messages
from .models import User

# This function will add and show User 
def add_show(request):
    if request.method == 'POST':
        form = StudentRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            student = User(name=name, email=email, password=password)
            messages.success(request, 'Created Successfull!')
            student.save()
            form = StudentRegister()
    else:
        form = StudentRegister()
    students = User.objects.all()
    return render(request, 'enroll/add.html', {'form': form, 'students': students})


# This fuction will update and edit 
def update_student(request, id):
    if request.method == 'POST':
        student = User.objects.get(pk=id)
        form = StudentRegister(request.POST, instance=student)
        if form.is_valid():
            messages.success(request, 'Student Updated Successfull !')
            form.save()
    else:
        student = User.objects.get(pk=id)
        form = StudentRegister(instance=student)
    return render(request, 'enroll/update.html', {'form': form})


# This function will delete 
def delete_student(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()
        messages.success(request, 'Delete Successfull !!')
        # return HttpResponseRedirect('/')
    else:
        messages.error(request, 'Error Not delete User !')
    return HttpResponseRedirect('/')