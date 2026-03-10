from django.db import models

class Portfolio(models.Model):
    image = models.ImageField()
    title = models.CharField
    link = models.CharField
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
