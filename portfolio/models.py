from django.db import models
import datetime
from accounts.models import CustomeUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Team_Members(models.Model):
    info = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    skills = models.ForeignKey(Skills,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='team_members',default='teacher.png')
    twitter = models.CharField(max_length=255,default='#')
    instagram = models.CharField(max_length=255,default='#')
    facebook = models.CharField(max_length=255,default='#')
    linkdin = models.CharField(max_length=255,default='#')
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.info.username
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio',default='default.png')
    title = models.CharField(max_length=90)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    price = models.IntegerField(default=0)
    project_date = models.DateTimeField(default=datetime.datetime.now())
    team_member = models.ForeignKey(Team_Members, on_delete=models.CASCADE)
    counted_views = models.IntegerField(default=0)
    counted_like = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
    def snip(self):
        return self.content[:20] + '...'
    
    def capt(self):
        return self.title.capitalize()
    
class Comment(models.Model):
    which_portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        
        ordering = ['-created_date']

    def __str__(self):
        return self.name

class Reply(models.Model):
    which_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
    

