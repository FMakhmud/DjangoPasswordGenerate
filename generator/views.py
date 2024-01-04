from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html', context={'password': '1234'})


def about(request):
    return render(request, 'generator/description.html')


def password(request):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "(){}[]+_-=|!@#$%^&*:.,?"

    all_characters = ""
    if request.GET.get('uppercase'):
        all_characters += uppercase

    if request.GET.get('symbols'):
        all_characters += symbols

    if request.GET.get('lowercase'):
        all_characters += lowercase

    if request.GET.get('numbers'):
        all_characters += numbers

    length = int(request.GET.get('length', 10))
    amount = 15

    for i in range(amount):
        password1 = "".join(random.sample(all_characters, length))

    return render(request, 'generator/password.html', context={'password': password1})
