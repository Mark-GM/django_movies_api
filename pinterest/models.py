from django.db import models

class Cast(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)

class CommonInfo(models.Model):
    casts = models.ManyToManyField(Cast, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    title = models.CharField(max_length=50)
    description= models.TextField(max_length=100)
    release_date = models.DateField()
    poster_image = models.ImageField(upload_to='pinterest_posters', blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True

class Movie(CommonInfo):
    pass

class Series(CommonInfo):
    episode = models.IntegerField()
    season = models.IntegerField()
