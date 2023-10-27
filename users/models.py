from django.db import models
from django.contrib.auth.models import AbstractUser



class UserManager(models.Manager):
    def create_user(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField('email', unique=True)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def name(self):
        return self.email