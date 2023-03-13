from django.db import models

class UrlData(models.Model):
    url = models.URLField()
    slug = models.CharField(max_length=10)

    def __str__(self):
        return self.url
