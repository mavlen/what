from django.urls import path
from .views import mess, registr, spisok, get_list

urlpatterns = [
    path('', mess,name ='message'),
    path('register/', registr, name='register'),   
    path('all/',spisok),    
    path('all/<int:pk>/', get_list , name='detail'),
]