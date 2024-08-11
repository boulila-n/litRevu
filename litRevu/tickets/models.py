from django.conf import settings
from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

PersonalUser = get_user_model()


class Ticket(models.Model):
    """
        Model tickets
    """
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2038, blank=True)
    user: PersonalUser = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                           on_delete=models.CASCADE)

    image = models.ImageField(upload_to='tickets/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('liste')


class Review(models.Model):
    """
        Model review
    """
    title_review = models.CharField(max_length=128)
    description_review = models.TextField(max_length=2038, blank=True)
    choices_note = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    note = models.CharField(max_length=10, choices=choices_note, default="1")
    ticket: Ticket = models.OneToOneField(to=Ticket,
                                          on_delete=models.CASCADE,
                                          related_name='reviews_rel')
    user: PersonalUser = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title_review}"
