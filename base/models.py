from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dp=CloudinaryField('image')
    bio=models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    image=CloudinaryField('image')
    name=models.CharField(max_length=20,null=True,blank=True)
    caption=models.TextField(null=True,blank=True)
    posted=models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    like= models.IntegerField(default=0)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return f'{self.name}'

class Followers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    another_user=models.ManyToManyField(User,related_name='another_user')

    def __str__(self):
        return f'{self.user.username}'

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField()
    update= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update','-created']

    def __str__(self):
        return self.body[0:50]
