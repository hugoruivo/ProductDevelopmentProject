from django.conf.urls import url

from . import views

app_name = 'api'
api_version = 'v1'

urlpatterns = [
    url(api_version + '/insurance/risktype/(?P<risk_type_id>\d+)', views.risktype, name='risktype'),
    url(api_version + '/insurance/risktype/', views.risktype, name='risktype'),
    url(api_version + '/insurance/get/(?P<insurance_id>\d+)', views.getdata, name='getdata'),
    url(api_version + '/insurance/get/', views.getdata, name='getdata')
]
