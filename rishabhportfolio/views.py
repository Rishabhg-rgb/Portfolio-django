from django.shortcuts import redirect, render
from .models import Contact
# Create your views here.


def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        project = request.POST['project']
        message = request.POST['message']
        contact = Contact(Name = name,Email = email, Phone = phone ,Project = project,Message = message)
        contact.save()
    return redirect('/')

def home(request):
    return render(request,'index.html')