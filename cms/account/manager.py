from typing import Any
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True
    
    
    def create_user(self,email,password=None,**extra_fields):
        if email==None:
            raise ValueError("email is required")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using =self._db)
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_superuser have is_staff must be true')
        
        
        return self.create_user(email,password,**extra_fields)