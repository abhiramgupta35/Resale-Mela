from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_seller=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)

class customeregister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    email=models.EmailField()

class sellregister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class category(models.Model):
    category_name = models.CharField(max_length=200)


    def __str__(self):
        return self.category_name



class productt(models.Model):
    seller = models.ForeignKey(sellregister, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=200)
    category_name = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.IntegerField()
    pic = models.ImageField(upload_to='products')
    Specification = models.TextField()
    purchased_year = models.IntegerField()


class CustomerRequest(models.Model):
    customer = models.ForeignKey(customeregister, on_delete=models.CASCADE, null=True, blank=True)
    pro = models.ForeignKey(productt, on_delete=models.CASCADE)
    card_number = models.IntegerField()
    cvv = models.CharField(max_length=3)
    payment_status = models.IntegerField(default=0)
    order_status = models.IntegerField(default=0)



class Cfeedback(models.Model):
    customer = models.ForeignKey(customeregister, on_delete=models.CASCADE, null=True, blank=True)
    feedback = models.CharField(max_length=200)

