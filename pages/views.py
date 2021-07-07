from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np
import json as js

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def instructions_view(request, *args, **kwargs):
    return render(request, "instructions.html", {})


def cropyield_view(request, *args, **kwargs):
    return render(request, "cropyield.html", {})


def cropvalue_view(request, *args, **kwargs):
    return render(request, "cropvalue.html", {})


def temprf_view(request, *args, **kwargs):
    return render(request, "temp_rf.html", {})


def predict_temp_rf(request, *args, **kwargs):
    if request.POST.get('action') == 'post':

        # Receive data from client
        month_input = float(request.POST.get('month_input'))
        year_input = float(request.POST.get('year_input'))

        # Unpickle model
        temp_model = pd.read_pickle(
            r".\temp_model.pickle")
        temp_result = temp_model.predict([[year_input, month_input]])
        temperature_pred = temp_result[0]

        rainfall_model = pd.read_pickle(
            r".\rainfall_model.pickle")
        rainfall_result = rainfall_model.predict([[year_input, month_input]])
        rainfall_pred = rainfall_result[0]

        print(temp_result)
        print(temperature_pred)
        print(rainfall_result)
        print(rainfall_pred)

    return JsonResponse({'result_temp': temperature_pred, 'result_rainfall': rainfall_pred, 'month_input': month_input, 'year_input': year_input}, safe=False)


def predict_crop_val(request, *args, **kwargs):
    if request.POST.get('action') == 'post':

        # Receive data from client
        crop_code_input = float(request.POST.get('crop_code_value'))
        year_input = float(request.POST.get('year_input_crop_value'))

        # Unpickle model
        cval_model = pd.read_pickle(
            r".\crop_value_model.pickle")
        cval_result = cval_model.predict([[crop_code_input, year_input]])
        cval_pred = cval_result[0]

    return JsonResponse({'result_value': cval_pred, 'year_input_crop_value': year_input, 'crop_code_value': crop_code_input}, safe=False)


def predict_crop_yield(request, *args, **kwargs):
    if request.POST.get('action') == 'post':

        # Receive data from client
        crop_code_input = float(request.POST.get('crop_code_yield'))
        year_input = float(request.POST.get('year_input_crop_yield'))

        # Unpickle model
        cyield_model = pd.read_pickle(
            r".\crop_yield_model.pickle")
        cyield_result = cyield_model.predict([[crop_code_input, year_input]])
        cyield_pred = cyield_result[0]

    return JsonResponse({'result_value': cyield_pred, 'year_input_crop_yield': year_input, 'crop_code_yield': crop_code_input}, safe=False)
