from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    datetime = models.DateTimeField()
    slug = models.SlugField()

    def __str__(self):
        return self.title