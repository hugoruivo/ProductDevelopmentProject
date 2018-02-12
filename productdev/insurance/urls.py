from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'risktype/', views.risktype, name='risktype')
]
