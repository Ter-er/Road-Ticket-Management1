from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class EmailAndLicenseAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, license_no=None, **kwargs):
        if username is None or license_no is None:
            return None
        
        try:
            # Check if the user exists in the database
            user = CustomUser.objects.get(email=username, license_no=license_no)
        except CustomUser.DoesNotExist:
            return None
        
        return user