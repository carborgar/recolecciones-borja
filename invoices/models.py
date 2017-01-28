from django.db import models
from customers.models import Customer
from datetime import date
from decimal import Decimal


class Invoice(models.Model):
    # Attributes
    # - Invoice attributes
    invoice_id = models.CharField(unique=True, max_length=6, null=True, blank=True)
    invoice_date = models.DateField(default=date.today)
    paid = models.BooleanField(default=False)

    # - Client data attributes (need to repeat because it's editable)
    invoice_to_id_number = models.CharField(max_length=255)
    invoice_to_name = models.CharField(max_length=255)
    invoice_to_address = models.CharField(max_length=255)
    invoice_to_postal_data = models.CharField(max_length=255)

    # Relationships
    customer = models.ForeignKey(Customer)

    def total(self):
        total = Decimal('0.00')
        for item in self.items.all():
            total = total + item.total()

        return total

    def __str__(self):
        return "Factura #{0.invoice_id}".format(self)

    class Meta:
        ordering = ["-invoice_date"]
        verbose_name = "factura"


class InvoiceItem(models.Model):
    # Attributes
    description = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)

    # Relationships
    invoice = models.ForeignKey(Invoice, related_name='items', unique=False)

    def total(self):
        total = Decimal(str(self.unit_price * self.quantity))
        return total.quantize(Decimal('0.01'))

    def __str__(self):
        return "{0.description} -> {0.quantity} * {0.unit_price}".format(self)

    class Meta:
        verbose_name = "línea de factura"
        verbose_name_plural = "líneas de factura"

