from django.db import models

# Create your models here.


class GuestInfo(models.Model):
    room_type = models.CharField()
    room_id = models.PositiveIntegerField()
    availability = models.BooleanField()
    full_name = models.CharField()
    address = models.CharField()
    email = models.EmailField()
    zipcode = models.PositiveIntegerField()
    state = models.CharField(max_length=2)
    phone = models.PositiveIntegerField()


class PaymentInfo(models.Model):
    company = models.CharField()
    card_number = models.PositiveIntegerField()
    csv = models.PositiveIntegerField(max_length=3)
    expiration = models.DateField(defalt="MM/YY")
    card_holder = models.CharField()
