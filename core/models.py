from django.db import models
from django.utils import timezone

# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")
    cv = models.ImageField(blank=True, null=True, upload_to="about", verbose_name="CV")
    
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill name")
    description = models.TextField(verbose_name="About skill")

    def __str__(self):
        return self.name

# Coding Skill Model
class CodeSkill(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name="Coding Skill Name")
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="skills")
    
    def __str__(self):
        return self.name

class SoftSkill(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name="Soft Skill Name")
    image = models.ImageField(blank=True, null=True, upload_to="skills")
    
    def __str__(self):
        return self.name

# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    description = models.TextField()    
    image = models.ImageField(upload_to="works")
    upload_time = models.DateTimeField(auto_now_add=True)
    
    def upload_time_ago(self):
        now = timezone.now()
        time_diff = now - self.upload_time
        if time_diff.days > 365:
            return '{} years ago'.format(time_diff.days // 365)
        elif time_diff.days > 30:
            return '{} months ago'.format(time_diff.days // 30)
        elif time_diff.days > 0:
            return '{} days ago'.format(time_diff.days)
        elif time_diff.seconds > 3600:
            return '{} hours ago'.format(time_diff.seconds // 3600)
        elif time_diff.seconds > 60:
            return '{} minutes ago'.format(time_diff.seconds // 60)
        else:
            return 'just now'
    def __str__(self):
        return self.title
    

class MyIcon(models.Model):
    webicon = models.FileField(blank=True, null=True, upload_to='home', verbose_name="WEB Icon")
    homebg = models.ImageField(blank=True, null=True, upload_to='home', verbose_name="Home Background")
    fb = models.FileField(blank=True, null=True, upload_to='home', verbose_name="FB Icon")
    insta = models.FileField(blank=True, null=True, upload_to='home', verbose_name="Insta Icon")
    twitter = models.FileField(blank=True, null=True, upload_to='home', verbose_name="Twitter Icon")
    linkedin = models.FileField(blank=True, null=True, upload_to='home', verbose_name="Linkedin Icon")
    
    class Meta:
        verbose_name = "My Icon"
        verbose_name_plural = "My Icon"

    def __str__(self):
        return "My Icon"

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)
    options = models.CharField(max_length=30)
    concern = models.TextField(max_length=30)

    def __str__(self):
        return self.name

