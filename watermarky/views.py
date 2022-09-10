from email import message
from  .models import Imaj
from . import forms
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from watermarky.forms import  UserForm



# Create your views here.
def home_view(request):
    konekte = request.user.is_authenticated
    context = {"konekte":konekte}
    return render(request,'home.html',context)


def konekte(request):
    if request.method == "POST":
        non = request.POST['non']
        modpas = request.POST['modpas']
        user = authenticate(username=non, password=modpas)
        if user is not None:
            login(request, user)
            print("Idantifyan konekte")

            return redirect('http://127.0.0.1:8000/upload/')
        else:
            print("No no")
            
    context = {}
    return render(request, "watermark.html", context)

def dekonekte(request):
    logout(request)
    print("Idantifyan dekonekte")
    
    return redirect('/')

def kreye_kont(request):
    # form = forms.UserForm()
    if request.method == 'POST':
         form = UserForm(request.POST)
         if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form=UserForm()
    return render(request, 'kreye_kont.html',context={'form':form})

def uploadImaj(request):
    if request.method == 'POST':
       
        pseudo = request.POST.get('pseudo')
        file = request.POST.get('img')

        # img = request.FILES.get('watermark-file')
        # Imaj.objects.create(photo=img)

        f = Imaj.objects.create(pseudo=pseudo, photo=file)
        f.save()
       
        
    return render(request, 'watermark.html')



       
def voir_im(request):
    ims = Imaj.objects.all()
    return render(request,'voir_im.html',{'ims':ims})     
