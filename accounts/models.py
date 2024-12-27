from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission, Group

# Create your models here.
from django.db import models

class CustomUserManager(BaseUserManager):

    def create_user(self, email, license_no, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not license_no:
            raise ValueError('The License Number field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, license_no=license_no, **extra_fields)
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    license_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10, unique=True, blank=True)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Permissions fields
    user_permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' # This is the field that is used for authentication
    REQUIRED_FIELDS = ['license_no'] # These fields are required when creating a user

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


