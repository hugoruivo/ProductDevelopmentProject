# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import os

# Create your views here.
def risktype(request, project_id=0):
    api_url_path = '/api/v1/insurance/risktype'
    if 'STAGE' in os.environ:
        api_url_path = '/' + os.environ['STAGE'] + '/api/v1/insurance/risktype'

    context = {'api_url_path': api_url_path}

    return render(request, 'insurance/risktype.html', context)
