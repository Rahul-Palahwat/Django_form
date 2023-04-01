from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    query = models.TextField()
    date = models.DateField()

    # to save the form with user name or whatever we want
    def __str__(self):
        return self.name
