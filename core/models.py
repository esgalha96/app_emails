from django.db import models

class Emails(models.Model):
    email = models.CharField(max_length=50, verbose_name="Email")

    def __str__(self):
        return self.email
