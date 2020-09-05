from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.shortcuts import reverse
from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have email address")
        user    =   self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def search(self):
        return self.get_queryset().search(query=query)

        
    def create_superuser(self, email, password):
        user    =   self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


GENDER_CHOICE = (
    ('male','Male'),
    ('female','Female'),
    ('others','Others')
) 
class User(AbstractBaseUser):
    email       =   models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name    =   models.CharField(max_length=30, blank=True)
    last_name    =   models.CharField(max_length=30, blank=True)
    gender      =   models.CharField(max_length=10, choices=GENDER_CHOICE)
    # bio         =   models.TextField(max_length=2000, blank=True, null=True)
    profile_pic =   models.ImageField(default='default/blank.png',
                        upload_to="users/%Y/%m/%d", blank=True, null=True)
    mobile      =   models.PositiveIntegerField(null=True, blank=True, unique=True)
    country     =   CountryField()
    is_admin    =   models.BooleanField(default=False)
    is_active   =   models.BooleanField(default=True) 
    is_staff    =   models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    date_joined =   models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login  =   models.DateTimeField(verbose_name="last login", auto_now=True)
    profession=models.CharField(max_length=300, blank=True,null=True)
    work_address=models.CharField(max_length=300, blank=True,null=True)
    city=models.CharField(max_length=300, blank=True,null=True)
    # postal_code=models.CharField(max_length=300, blank=True,null=True)
    is_shadow_banned = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    is_investor=models.BooleanField(default=False)

    ''' setting the email as the required login field,
    but we can also user username if we so wish '''
    USERNAME_FIELD = 'email'

    objects =  UserManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Verification(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='verified_users')
    national_Id=models.PositiveIntegerField(unique=True)
    front_Id=models.ImageField(upload_to='Id_Pics')
    back_Id=models.ImageField(upload_to='Id_Pics')
    proof=models.ImageField(upload_to='Id_Pics')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'Verification details for {self.user.email}'
