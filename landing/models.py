from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=128)

    def __str__(self):

            return '%s %s' % (self.email, self.name)
    class Meta:
        verbose_name = "My Subscriber"
        verbose_name_plural = "Subscribers"





