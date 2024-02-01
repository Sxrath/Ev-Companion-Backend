from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    #Model representing a location.
    place = models.CharField(max_length=100, unique=True)
    
    # def __str__(self) -> str:
    #     return self.place
class Chargingspot(models.Model):
    # Model representing a charging spot.
    name = models.CharField(max_length=50, default=None)
    place = models.ForeignKey(Location, on_delete=models.CASCADE)
    station = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6 , blank=True,default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,default=0.0)
    
    # def __str__(self) -> str:
    #     return f'{self.name} -- {self.station}'
    
class Reservation(models.Model):
    # Model representing a reservation for a charging spot.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    chargingspot = models.ForeignKey(Chargingspot, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ['starttime']

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chargingspot = models.ForeignKey(Chargingspot, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.chargingspot.name}"
    
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=1000)
    date_posted=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.content}'
    
class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user} to '{self.post.content}'"


