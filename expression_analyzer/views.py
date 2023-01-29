from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import render
import urllib
import base64 
import logging
from urllib.request import urlopen
from expression_analyzer.exe import getExpression
import cv2
from tensorflow.keras.models import model_from_json
import numpy as np
from PIL import Image
import glob

logger = logging.getLogger(__name__)

def home(request):
    context = dict()
    if request.method == 'POST':
        image = request.POST['src']
        response = urllib.request.urlopen(image)
        with open('image.jpg', 'wb') as f:
            f.write(response.file.read())
        
        print(request.POST)

        print(getExpression('/home/dev007/DEV007/Projects/music_recommendation_system/face_listen/image.jpg'))
        if image is not None:
            print('Image is not null')
    return render(request, 'expression_analyzer/expression_analyzer.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.        