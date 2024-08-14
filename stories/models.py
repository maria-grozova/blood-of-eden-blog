from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

APPROVAL = ((0, "Draft (Top Secret)"),
            (1, "Published (Approved for Distribution)"))


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

    class Meta:
        ordering = ["-created_on", "author"]

    def __str__(self):
        return f"{self.title}, written by {self.author}"


class Comment(models.Model):
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approval = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on", "author"]

    def __str__(self):
        return f"{self.author} rated {self.rating} out of 10 and said: {self.body[:20]}"
