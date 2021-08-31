import joblib as jb
import json
from django.http import HttpResponse
from django.http import JsonResponse


def Prediction(request) :
    path = "MetaData/Model/Model.sav"
    model = jb.load(path)
    inputs = []
    inputs.append(request.GET['year'])
    inputs.append(request.GET['month'])
    inputs.append(request.GET['state'])
    inputs.append(request.GET['variety'])
    predictionArray = model.predict([inputs])
    prediction = { "prediction" : predictionArray[0]}
    return JsonResponse(prediction)

def home(request):
    return HttpResponse("<html><body></body></html>")



