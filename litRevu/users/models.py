from django.contrib.auth.models import AbstractUser
from django.db import models


class PersonalUser(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES,
                            verbose_name='Rôle', default=CREATOR)
    # Subscribes
    subscribes = models.ManyToManyField("self", symmetrical=False, blank=True,
                                        related_name="followers")

    def __str__(self):
        return self.username
