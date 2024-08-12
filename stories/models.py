from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

APPROVAL = ((0, "Draft (Top Secret)"), (1, "Published (Approved for Distribution)"))

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stories"
    )
    tags = TaggableManager()
    content = models.TextField()
    feature = models.TextField(null=True, blank=True)
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approval = models.IntegerField(choices=APPROVAL, default=0)