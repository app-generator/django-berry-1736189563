# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Edr(models.Model):

    #__Edr_FIELDS__
    edr = models.CharField(max_length=255, null=True, blank=True)

    #__Edr_FIELDS__END

    class Meta:
        verbose_name        = _("Edr")
        verbose_name_plural = _("Edr")


class Image_Det(models.Model):

    #__Image_Det_FIELDS__
    image_det = models.CharField(max_length=255, null=True, blank=True)

    #__Image_Det_FIELDS__END

    class Meta:
        verbose_name        = _("Image_Det")
        verbose_name_plural = _("Image_Det")



#__MODELS__END
