from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    phone_number = models.CharField(max_length=10, null=True)
    re_password = models.CharField(max_length=128, verbose_name='re-password', null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    cr_date = models.DateTimeField(auto_now_add=True, null=True)
    upd_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_master'
