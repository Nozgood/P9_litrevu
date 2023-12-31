from django.db import models
from litrevu import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    """
    Ticket represents a ticket in our application
    """
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Review(models.Model):
    """
    Review represents a review in our application
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    headline = models.TextField(max_length=8192, blank=True)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
