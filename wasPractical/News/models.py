from django.db import models


class News(models.Model):
    title = models.TextField(max_length=128)
    author = models.TextField(max_length=128)
    date = models.DateField(default=0)
    text = models.TextField(max_length=1024)

    def __str__(self):
        return self.title
    # Create your models here.
