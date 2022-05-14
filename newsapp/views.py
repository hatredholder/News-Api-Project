import requests
from django.shortcuts import render


def index(request):
    r = requests.get("http://api.mediastack.com/v1/news?access_key=805173b20a70e695012f67f73b75a0f9&countries=ru")
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i["image"])
        url.append(i["url"])
    news = zip(title, description, image, url)
    return render(request, 'newsapp/index.html', {'news':news})