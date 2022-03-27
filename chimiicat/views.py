from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static
from django.core.mail import send_mail
from django.http import FileResponse, Http404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import base64
import datetime
import time
import json

from . import settings

def home(request):
    return render(
        request,
        'home.html',
    )

def shop(request):
    with open('static/data/vga.json', 'r') as file:
        items = json.load(file)
    return render(
        request,
        'shop.html',
        { 'items': items }
    )
