from django.contrib import admin
from django.urls import path
from . import views



    
urlpatterns = [
    path('',views.home_view),
    path('konekte/',views.konekte, name='konekte'),
    path('dekonekte/',views.dekonekte, name='dekonekte'),
    path('kreye_kont/',views.kreye_kont),
    path('upload/',views.uploadImaj,name="upload"),
    # path('/voir_im/',views.voir_im)
]
