from django.db import models

class Query(models.Model):
    intent = models.CharField(max_length=50)
    response = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Intent: ' + self.intent