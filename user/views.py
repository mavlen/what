from django.shortcuts import render

from user.models import Name
from .forms import Regform

def mess(request):
    return render(request, 'hello.html')

def registr(request):
    form = Regform(request.POST or None)
    message = 'Заполните поля'
    if request.method == 'POST' and form.is_valid():
        message = 'Операция успешна выполнена'
        form.save()
        return render(request, 'hello.html', {'form': form, 'message':message})
    return render(request, 'hello.html', {'form': form, 'message':message})


def get_list(request):
    reg = Name.objects.all()
    return render(request, 'spisok.html', {'reg':reg})

def user_detail(request, pk):
    details = Name.objects.filter(pk=pk)
    return render(request, 'details.html', {'details':details})