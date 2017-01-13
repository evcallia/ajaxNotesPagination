from __future__ import unicode_literals

from django.db import models
import re  #regex
# from django.contrib import messages #to display errors
# import bcrypt  #encryption
# from datetime import datetime
# from django.core.exceptions import ValidationError

class Note(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
