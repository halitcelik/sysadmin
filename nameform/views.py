# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return render(request, 'home.html', {'name': name})
    else:
        return render(request, 'save-name.html')
