from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

# class User(AbstractUser):
#     pass


class Chore(models.Model):
    title = models.CharField('Title', max_length=120)
    master = models.ForeignKey("Person", on_delete=CASCADE, related_name="master")
    slave = models.ForeignKey("Person", on_delete=CASCADE, related_name="slave")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    task = models.CharField('Task', max_length=500, default="empty")

class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ROLE_CHOICES=(
        ('Master', 'Master'),
        ('Slave', 'Slave'),
    )
    role  = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username

# class Master(models.Model):
#     user = models.OneToOneField(User, on_delete=CASCADE)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Slave(models.Model):
#     user = models.OneToOneField(User, on_delete=CASCADE)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)