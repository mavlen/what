from django.urls import path
from .views import mess, registr, get_list, user_detail

urlpatterns = [
    path('', mess,name ='message'),
    path('register/', registr, name='register'),   
    path('all/',get_list),    
    path('all/<int:pk>/', user_detail , name='detail'),
]