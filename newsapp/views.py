import requests
from django.shortcuts import render


def index(request):
    r = requests.get("https://api.mediastack.com/v1/news?access_key=YOUR_ACCESS_KEY&countries=ru")
    res = r.json()
    data =