from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)  # Hex color code
    type_body = models.ForeignKey('typebody.TypeBody', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name