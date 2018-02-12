# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Insurancetype, Insurance

import json
import datetime

# Create your views here.
def risktype(request, risk_type_id=0):
    if(int(risk_type_id) == 0):
        all_entries = Insurancetype.objects.all()

        json_res = []
        for entry in all_entries:
            json_res.append(entry.get_json())

        return JsonResponse({'results': json_res})
    try:
        i_type = Insurancetype.objects.get(pk=risk_type_id).get_json()
        return JsonResponse({'results': [i_type]})
    except Insurancetype.DoesNotExist:
        return JsonResponse({'results': []})

    return JsonResponse({'results': []})

def getdata(request, insurance_id=0):
    try:
        insur = Insurance.objects.get(pk=insurance_id).get_json()
        return JsonResponse({'results': insur})
    except Insurance.DoesNotExist:
        return JsonResponse({'results': []})

    return JsonResponse({'results': []})
