
from django.urls import path
from .views import home, say_hello

urlpatterns = [
    path('',home, name="home" ),
    # path('say_hello',say_hello, name="say_hello" ),
    # path('success',success, name="success" ),
    path('say_hello',say_hello, name="say_hello" ),
    
]
