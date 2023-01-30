from django.db import models


class RadioButtonModel(models.Model):
    day = models.CharField(max_length=100)


class WorkSpaceModel(models.Model):
    name = models.CharField(max_length=100)
    prototype = models.CharField(max_length=100)
    day = models.ForeignKey(RadioButtonModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} <{self.prototype}>"
