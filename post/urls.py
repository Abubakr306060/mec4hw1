from django.urls import path
from .views import *

urlpatterns = [
    path('hi/', hello),
    path('goodbye/',goodbye ),
    path("",gobal),
    path("about/",about),
    path("",gobal),
    path("time/",time),


]
