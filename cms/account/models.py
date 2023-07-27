from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from tinymce.models import HTMLField
from cms import common


# Create your models here.
class CustomUser(AbstractUser):
    username=None
    name=models.CharField( max_length=250)
    address=models.CharField( max_length=250)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=255,unique=True)
    
    

    role = models.CharField(max_length=20, choices=common.USER_ROLES)

    
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = []
    
    objects=UserManager()
    
    

    
    
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    tag=models.CharField( max_length=255)
    
    
class Category(models.Model):
    name=models.CharField( max_length=50)
    slug=models.SlugField()
    description=models.TextField()
    
class Post(models.Model):
    title = models.CharField(max_length= 100)
    content =HTMLField()
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    thumbnail=models.ImageField()
    
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    Tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)

    
