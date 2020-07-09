from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home page'),
    path('naam',views.naam,name='naam page'),
    path('x',views.x,name='x value')
]
