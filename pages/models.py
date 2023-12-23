from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Vote(models.Model):

    candidates = [
        ("sandeep", "Sandeep Maheshwari"),
        ("vivek", "Dr. Vivek Bindra"),
    ]

    vote_for = models.CharField(choices=candidates, max_length=10)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.vote_for + " - " + self.user.email
