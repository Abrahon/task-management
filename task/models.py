from django.db import models
from django.utils import timezone

# Create your models here.
class TaskStoreModel(models.Model):
    
    STATUS = [
        ('complete','complete'),
        ('incomplete','incomplete'),
    ]
    
    PRIORITY = [
        ('Low','Low'),
        ('Normal','Normal'),
        ('High','High')
    ]
    
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=110)
    status = models.CharField(max_length=10, choices=STATUS)
    priority = models.CharField(max_length=10, choices=PRIORITY)
    due_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    start_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
