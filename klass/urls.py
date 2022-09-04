from django.urls import path
from .import views


urlpatterns = [

    path('',views.say_hello,name='home'),
    path('add',views.add,name='add')
] 