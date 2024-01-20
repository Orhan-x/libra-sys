from collections.abc import Iterable
from django.db import models

class Registration(models.Model):
    
    cni          = models.CharField(primary_key=True, max_length = 10, unique=True)
    f_name       = models.CharField(max_length = 255)
    l_name       = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 10)
    email        = models.EmailField()

    def save(self, *args, **kwargs):
        
        self.cni = self.cni.upper()
        
        self.f_name = self.f_name.capitalize()
        
        self.l_name = self.l_name.upper()
        
        self.email  = self.email.lower()
        
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.f_name + self.l_name