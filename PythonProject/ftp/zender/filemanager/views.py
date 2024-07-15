# filemanager/views.py

import os
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings


def index(request):
    files = os.listdir(settings.MEDIA_ROOT)
    #return HttpResponse("Welcome")
    files[0]
    return render(request, 'index.html', {'files': files})

def download(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
