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

# class FacialExpressionModel(object):
#     EMOTIONS_LIST = ["Angry", "Disgust",
#                     "Fear", "Happy",
#                     "Neutral", "Sad",
#                     "Surprise"]
#     def __init__(self, model_json_file, model_weights_file):
#         # load model from JSON file
#         with open(model_json_file, "r") as json_file:
#             loaded_model_json = json_file.read()
#             self.loaded_model = model_from_json(loaded_model_json)
#         # load weights into the new model
#         self.loaded_model.load_weights(model_weights_file)
#         self.loaded_model.make_predict_function()
#     def predict_emotion(self, img):
#         self.preds = self.loaded_model.predict(img)
#         return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]

# facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# model = FacialExpressionModel("model.json", "model_weights.h5")
# font = cv2.FONT_HERSHEY_SIMPLEX


# def getExpression(path):
#     if(path is NULL):
#         path = '/home/dev007/DEV007/Projects/music_recommendation_system/face_listen/image.jpg'
#     fr = cv2.imread(path)
#     gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
#     faces = facec.detectMultiScale(gray_fr, 1.3, 5)
#     for (x, y, w, h) in faces:
#         fc = gray_fr[y:y+h, x:x+w]
#         roi = cv2.resize(fc, (48, 48))
#         pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
#         print("------------------------------------------")
#         print(pred)
#         print("------------------------------------------")
#         cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
#         cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
#     return fr



logger = logging.getLogger(__name__)


def home(request):
    logger.info("Heleohwihoworwq")

    logger.info("Keel  bro")
    print('Hello broo')

    context = dict()
    if request.method == 'POST':
        # print('Hello Inside POSt')
        # print(request.POST)
        # image_path = request.POST["src"] 
        # print(len(image_path))
        # print("666666666666666666666666666666666666666666")

       

        # # Decode base64 String Data
      

        
        # # print(png_recovered)
        # print('fff')
        # print(image_path)

        # print(type(image_path))
        #  # src is the name of input attribute in your html file, this src value is set in javascript code
        # image = NamedTemporaryFile()
        # image = File(image)
        # name = str(image.name).split('\\')[-1]
        # name += '.jpg'  # store image in jpeg format
        # image.name = name
        # print(image.name)

        # image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        # image = NamedTemporaryFile()
        # image.write(urlopen(image_path).read())
        # image.flush()
        # image = File(image)
        # name = str(image.name).split('\\')[-1]
        # name += '.jpg'  # store image in jpeg format
        # image.name = name
        # webimg = ""
        # webimg =  urlopen(request.POST["src"])
        # data = webimg.read()
        # content_file = ContentFile( data, "webcam.jpg" )

        # response = urllib.request.urlopen(webimg)
        # with open('wcc2.jpg', 'wb') as f:
        #     f.write(response.file.read())

        image = request.POST['src']
        response = urllib.request.urlopen(image)
        with open('image.jpg', 'wb') as f:
            f.write(response.file.read())
        
        print(request.POST)

        print(getExpression('/home/dev007/DEV007/Projects/music_recommendation_system/face_listen/image.jpg'))
        

        # print(request.POST[''])
        # print('Get Image')
        if image is not None:
            print('Image is not null')
            # print(image)
    else:
        print('No Post')
    return render(request, 'expression_analyzer/expression_analyzer.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.        