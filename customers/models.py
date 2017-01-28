from django.db import models


class Customer(models.Model):
    # Attributes
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    province = models.CharField(max_length=255)

    def __str__(self):
        return "{0.name} ({0.id_number})".format(self)

    class Meta:
        ordering = ["name"]
        verbose_name = "cliente"
