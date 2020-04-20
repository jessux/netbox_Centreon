from django.db import models

class CentreonObjectStatus(models.Model):
    name = models.CharField(max_length=50)
    imported = models.BooleanField(default=False)
    state= models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def isimported(self):
        return self.imported

    def isactivated(self):
        return self.state