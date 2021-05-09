from django.db import models
from django.contrib.auth.models import AbstractUser



class Designation(models.Model):
    designation_name= models.CharField(max_length=250)

    def __str__(self):
        return self.designation_name 


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    contact = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=250)
    is_verified = models.BooleanField(default=True)
    designation_name = models.ForeignKey(Designation,on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class UserControlTable(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uct_supervisor')
    supervised = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uct_supervised')
            

class ClientType(models.Model):
    client_type_name = models.CharField(max_length=250)

    def __str__(self):
        return self.client_type_name

class ClientTable(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact_no = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    anniversary_date = models.DateField()
    occupation = models.CharField(max_length=250)
    client_type_id = models.ForeignKey(ClientType,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='updated_by')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name