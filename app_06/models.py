from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .validation import validate_bad_words, validate_email, validate_age, bad_words
from django.core import validators
from django.core.exceptions import ValidationError

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        unique=True,
        validators=[
            validate_email,
            validators.EmailValidator(message="Enter a valid email"),
        ],
    )
    bio = models.TextField(blank=True, validators=[validate_bad_words])
    age = models.PositiveIntegerField(validators=[validate_age])
    joined_at = models.DateTimeField(default=timezone.now)

    def save(self):
        self.full_clean()
        return super().save()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username", "-joined_at"]  # - reverse order
        constraints = [
            models.UniqueConstraint(
                fields=["username", "email"], name="unique username/email"
            )
        ]
        db_table = "users_06"
        verbose_name = "users from the app"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    PUBLIC = "public"
    PRIVATE = "private"
    VISIBILITY_CHOICES = [
        (PUBLIC, "Public"),
        (PRIVATE, "Private"),
    ]
    visibility = models.CharField(
        max_length=10, choices=VISIBILITY_CHOICES, default=PUBLIC
    )

    class Meta:
        #saving the data at this order
        ordering = ["created_at"]
        verbose_name = "user post"
        db_table = "posts"

    def clean(self):
        if len(self.post) < 10:
            raise ValidationError("POst length must be at least 10")
        for word in bad_words:
            if word in self.post.lower():
                raise ValidationError("No bad words")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.post
