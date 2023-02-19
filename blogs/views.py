
from django.shortcuts import render, get_object_or_404
from .models import Patient
from django.core.files.storage import FileSystemStorage

import cv2
# import tensorflow as tf
# from tensorflow import keras
# from keras import layers
import numpy as np
import pandas as pd

from keras.models import load_model
from tensorflow.keras.models import load_model


# load ML model
model = load_model("C:/Users/prabo/Desktop/django/blogs/ML_model/final.h5")

def makeprediction(path):
    result = "" # to store the result of prediction

    img = cv2.imread(path)  # will give a numpy array
    # OpenCV gives colors in BGR, but we need colors in RGB

    # convert colors from BGR to RGB
    normal_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # to resize the image (244 x 244)
    final_img = cv2.resize(normal_img, (224, 224))

    # store the final_img in a numpy array and divide every value by 255
    image = np.array(final_img) / 255.0

    data = np.array([image])

    predict = model.predict(data)

    # return the indices of the maximum value on an axis
    predict_max = np.argmax(predict, axis=1)

    if predict_max == 1:
        print('NO DR')
        result = "No DR"
    else:
        print('DR')
        result = "DR"

    return result



# Create your views here.
def home(request):
    patient_info_all = Patient.objects.all()

    data = {
        'patient_info_all': patient_info_all
    }
    return render(request, 'home.html', data)


def index(request):
    return render(request, 'index.html')


def more_details(request, patient_id):
    path = ""
    res = ""
    filename = ""

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filename = fs.url(filename)
        
        path = "C:/Users/prabo/Desktop/django/blogs" + filename
            
        res = makeprediction(path)

    object = get_object_or_404(Patient, pk=patient_id)

    

    data = {'prediction': res, 'fileName': filename, 'current_patient': object}
    return render(request, 'more_details.html', data)
