from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import WorkSpaceModel, RadioButtonModel

# Register your models here.


admin.site.register(WorkSpaceModel)
admin.site.register(RadioButtonModel)
