from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/images/')
    url_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


