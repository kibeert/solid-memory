from django.shortcuts import render, redirect


# Create your views here.
from pytube import *

def youtube(request, *args, **kwargs):
    if request.method == "POST":
        link = request.POST['link']
        video = youtube(link)

        stream = video.streams.get_lowest_resolution()

        stream.download()

        return render(request, 'base/index.html')
    return render(request, 'base/index.html')