from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    # Makes the name of the Category model plural when used in a plural context
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return self.user.username