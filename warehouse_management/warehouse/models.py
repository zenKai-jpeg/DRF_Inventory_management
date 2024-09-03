from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    CATEGORY_CHOICES = [
        ('Electronic', 'Electronic'),
        ('Furniture', 'Furniture'),
        ('Clothing', 'Clothing'),
    ]
    
    STORAGE_CHOICES = [
        ('A', 'Storage A'),
        ('B', 'Storage B'),
        ('C', 'Storage C'),
        ('D', 'Storage D'),
    ]
    
    product_sku = models.CharField(max_length=100, unique=True, editable=False)  # Set editable=False
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Electronic')
    quantity = models.IntegerField()
    location = models.CharField(max_length=1, choices=STORAGE_CHOICES, default='A')
    supplier = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'inventories'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.product_sku:
            self.product_sku = f"PRD{self.id:03d}"
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_sku} - {self.name}"

class Inbound(models.Model):
    STORAGE_CHOICES = [
        ('A', 'Storage A'),
        ('B', 'Storage B'),
        ('C', 'Storage C'),
        ('D', 'Storage D'),
    ]

    product_sku = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    reference = models.CharField(max_length=10, editable=False) 
    quantity_received = models.IntegerField()
    date_received = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=1, choices=STORAGE_CHOICES, default='A')
    remarks = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            # Get the last entry's reference number and increment it
            last_inbound = Inbound.objects.order_by('id').last()
            if last_inbound:
                last_reference = last_inbound.reference
                reference_number = int(last_reference.split('INBOUND')[1]) + 1
            else:
                reference_number = 1  # start with 1 if no entries exist
            self.reference = f'INBOUND{reference_number:03d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_sku} to {self.location}"

class Outbound(models.Model):
    product_sku = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    reference = models.CharField(max_length=10, editable=False) 
    quantity_shipped = models.IntegerField()
    date_shipped = models.DateField(auto_now_add=True)
    destination = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.reference:
            # Get the last entry's reference number and increment it
            last_outbound = Outbound.objects.order_by('id').last()
            if last_outbound:
                last_reference = last_outbound.reference
                reference_number = int(last_reference.split('OUTBOUND')[1]) + 1
            else:
                reference_number = 1  # start with 1 if no entries exist
            self.reference = f'OUTBOUND{reference_number:03d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} to {self.customer}"