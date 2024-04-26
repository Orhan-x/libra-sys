from django.utils.translation import gettext_lazy as _
from django.db import models
from django import forms
class Registration(models.Model):
    
    cni          = models.CharField(primary_key=True, max_length = 10, unique=True, name="cni",verbose_name="CNIE",
                                    help_text="Upper or Lower cases isn't matter",
                                    error_messages={'unique': "This CNIE is already Exists! (ByMe)"}
                                    )
    f_name       = models.CharField(max_length = 255, error_messages={'required':"REQUIRED"},help_text="FirstName")
    l_name       = models.CharField(max_length = 255, blank=True)
    phone_number = models.CharField(max_length = 10, blank=True)
    email        = models.EmailField(blank=True)

    def save(self, *args, **kwargs):
        
        self.cni = self.cni.upper()
        
        self.f_name = self.f_name.capitalize()
        
        self.l_name = self.l_name.upper()
        
        self.email  = self.email.lower()
        
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f"{self.f_name} {self.l_name}"