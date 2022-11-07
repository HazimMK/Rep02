from django.urls import path
from .import views


urlpatterns= [ 
    path('myprjct/',views.fun1,name="prjct")
]