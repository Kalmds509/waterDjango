from email import message
from multiprocessing import context
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

                return redirect('/')
            else:
                print("No no")
    
        context = {}
        return render(request, "konekte.html",context)

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
        file = request.FILES.get('img')

        
        f = Imaj.objects.create(pseudo=pseudo, photo=file)
        f.save()
       
        
    return render(request, 'watermark.html')



       
def voir_im(request):
    ims = Imaj.objects.all()
    return render(request,'voir_im.html',{'ims':ims})     

def li_yon_atik(request,id):
    li = Imaj.objects.get(id=id)
    li.total_vizit += 1 
    li.save()
    context={'li':li}

    return render(request,'atik_lan.html',context)

