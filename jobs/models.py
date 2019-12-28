from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    link = models.URLField(blank=True,null=True)
    summary = models.CharField(max_length=200)
    
    def __str__(self):
        return self.summary[:20]

class Intro(models.Model):
    designation = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=100)
    title_of_detail = models.CharField(max_length=200)
    description = models.TextField()
    skills_desc = models.CharField(max_length=300)
  
    def __str__(self):
        return self.designation