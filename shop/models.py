from django.db import models


# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    odr_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=10000, default="")
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=90, default="")
    address = models.CharField(max_length=90, default="")
    city = models.CharField(max_length=90, default="")
    state = models.CharField(max_length=90, default="")
    zip = models.CharField(max_length=90, default="")
    phone = models.CharField(max_length=10, default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    odr_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:17] + "..."
