from django.db import models

# Create your models here.


class GuestandPaymentInfo(models.Model):
    room_type = models.CharField(max_length=250)
    room_id = models.PositiveIntegerField()
    availability = models.BooleanField()
    full_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField()
    zipcode = models.PositiveIntegerField()
    state = models.CharField(max_length=2)
    phone = models.PositiveIntegerField()
    company = models.CharField(max_length=250)
    card_number = models.PositiveIntegerField()
    csv = models.PositiveIntegerField()
    expiration = models.DateField(default="MM/YY")
    card_holder = models.CharField(max_length=250)