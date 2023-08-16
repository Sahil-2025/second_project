from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    date = models.DateField()
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
    
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, unique=True)


    def __str__(self):
        return self.first_name+' '+self.last_name



#class first_name(models.Model)

