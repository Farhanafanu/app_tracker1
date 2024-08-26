from django.db import models
from django.contrib.auth.models import User
class App(models.Model):
    image = models.ImageField(upload_to='app_images/', default='app_images/default.png')  
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, default='http://example.com')  
    sub_category = models.CharField(max_length=100,default='Default Category')
    points = models.PositiveIntegerField()
    category = models.CharField(max_length=50, default='Default Category')

    def __str__(self):
        return self.name



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    points_earned = models.PositiveIntegerField(default=0)  
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.app.name} - {self.points_earned} points"

