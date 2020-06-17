from django.db import models

# Create your models here.
class Person(models.Model):
    # persons_person
    name = models.CharField(max_length=150)
    pastjob = models.TextField()
    
    def __str__(self):
        return f'{self.id} - {self.name} : {self.pastjob}'
