from django.shortcuts import render
from .forms import StudentRegister
from django.contrib import messages
from .models import User

# Create your views here.
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
