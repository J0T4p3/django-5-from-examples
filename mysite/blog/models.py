from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


# A custom manager for the published Post model.
class PublishedManager(models.Manager):
    # Overwriting the base query function on the manager
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    # Equivalent to a enum class
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    # Slug is a alphanumeric with hyphen text. Useful for SEO
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # Receive the data auto when created
    created = models.DateTimeField(auto_now_add=True)
    # Receive the data auto when updated
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        # Results will be returned in reverse cronological publish order by default
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['publish'])
        ]

    # A unified way to resolve the url for Post data
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[self.publish.year, self.publish.month,
                  self.publish.day, self.slug]
        )

    def __str__(self):
        return f"{self.title} by {self.author.username} in {self.publish}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __repr__(self):
        return f'Comentário por {self.name}, em {self.post}'
