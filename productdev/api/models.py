# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.
class Insurancetype(models.Model):
    title = models.CharField(max_length=200)
    model = models.TextField()
    def __str__(self):
        return self.model

    def get_json(self):
        json_string = self.model
        obj = json.loads(json_string)
        json_obj = {
            'Insurance Type' : self.title,
            'Data' : obj
        }

        return json_obj

    class Meta:
        db_table = 'Insurancetype'

class Insurance(models.Model):
    insurance_type = models.ForeignKey(Insurancetype, on_delete=models.CASCADE)
    content = models.TextField()

    def get_json(self):
        json_string = self.content
        obj = json.loads(json_string)
        json_obj = {
            'Insurancetype Id': self.insurance_type_id,
            'Content' : obj
        }

        return json_obj

    class Meta:
        db_table = 'Insurance'
