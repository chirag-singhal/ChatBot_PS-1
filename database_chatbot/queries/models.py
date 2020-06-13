from django.db import models

class Query(models.Model):
    intent = models.CharField(max_length=2000)
    response = models.CharField(max_length=5530)
    
    def __str__(self):
        return 'Intent: ' + self.intent