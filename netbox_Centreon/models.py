from django.db import models

class CentreonObjectStatus(models.Model):
    ip = models.CharField(max_length=16)
    imported = models.BooleanField(default=False)
    state= models.BooleanField(default=False)

    def __str__(self):
        return self.ip

    def isimported(self):
        return self.imported

    def isactivated(self):
        return self.state