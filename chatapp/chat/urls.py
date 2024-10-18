from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<str:room>/',views.room,name='room'),
    path('check',views.check,name='check'),
    path('send',views.send,name='send'),
    path('getmsg/<str:room>/',views.getmsg,name='getmsg')
]