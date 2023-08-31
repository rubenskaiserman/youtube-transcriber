from django.db import models

class Transcriber_Model_Template(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    