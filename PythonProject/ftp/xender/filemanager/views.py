# filemanager/views.py

import os
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings
from pathlib import Path 


def index(request):
    files = [ [Path(f).stem , f ]  for f in os.listdir(settings.MEDIA_ROOT) if os.path.isfile(os.path.join(settings.MEDIA_ROOT, f))]
    return render(request, 'index.html', {'files': files})

def download(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
