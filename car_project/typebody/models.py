from django.db import models

class TypeBody(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type