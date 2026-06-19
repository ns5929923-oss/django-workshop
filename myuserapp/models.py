from django.db import models

class student(models.Model):
    Name = models.CharField()
    Email = models.EmailField()
    Mobile = models.CharField(max_length=10)
    Age = models.CharField()
    Address = models.CharField()

    def __str__(self):
        return self.Name