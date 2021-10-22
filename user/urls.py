from django.urls import path
from .views import mess, registr

urlpatterns = [
    path('', mess,name ='message'),
    path('9/', registr, name='register'),        
]