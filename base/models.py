from random import choices
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# ---------------------------------------------------------------------------------------- #
class Address(models.Model):
    country = models.TextField(max_length=200, null=True, blank=True)
    province = models.TextField(max_length=200, null=True, blank=True)
    district = models.TextField(max_length=200, null=True, blank=True)
    ward = models.TextField(max_length=200, null=True, blank=True)
    exact_address = models.TextField(max_length=200)
    
    class Meta:
        pass
    def __str__(self):
        return self.exact_address

# ---------------------------------------------------------------------------------------- #

class User(AbstractUser):

    customer_or_employee_choice = [
        ('Employee', 'Employee'),
        ('Customer', 'Customer')
    ]
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)

    avatar = models.ImageField(null=True, default="avatar.png")
    full_name = models.TextField(max_length=100, null=True, blank=True)
    SDT = models.CharField(max_length=20, null=True, blank=True)
    adress = models.ManyToManyField(Address, blank=True)

    customer_or_employee = models.CharField(
        max_length=100, 
        choices=customer_or_employee_choice,
        default='Customer',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
# ---------------------------------------------------------------------------------------- #
class Customer(User):

    class Meta:
        pass
    def __str__(self):
        return f"{self.full_name}"

# -----------------------------------------------------------------------------------------#
class Employee(User):
    position_choice = [
        ('Shipper','Shipper'),
        ('Product manager', 'Product Manager'),
        ('Employee manager', 'Employee Manager'),
        ('Order manager', 'Order manager')
    ]
    position = models.TextField(
        max_length=100,
        choices = position_choice,
        null=True, blank=True,
    )
    salary = models.IntegerField(default=0, help_text='VND')

    class Meta: 
        pass

# ---------------------------------------------------------------------------------------- #
class Category(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------------------- #
class Product(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, default = "default.png")
    description = models.TextField(null=True, blank= True)
    price = models.IntegerField()
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering  = ['-updated', '-created']

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------------- #
class Book(Product):
    company = models.TextField(null=True, blank=True)
    publish_date = models.DateField()
    width = models.FloatField(null=True, blank=True, help_text='cm')
    height = models.FloatField(null=True, blank=True, help_text='cm')
    number_page = models.IntegerField(null=True, blank=True)
    author = models.TextField(null=True,blank=True)
    book_category = models.TextField()
    # class Meta:
    #     # proxy = True
    #     pass

# ---------------------------------------------------------------------------------------- #
class MobilePhone(Product):
    bluetooth_choice = [
        ('Yes', 'yes'),
        ('No', 'no')
    ]
    brand = models.TextField(null=True, blank=True, )
    gen = models.TextField(null=True, blank=True, )
    pin = models.IntegerField(null=True, blank=True, default=None, help_text='mAh')
    screen_type = models.TextField(null=True, blank=True, )
    screen_size = models.FloatField(null=True, blank=True, default=None, help_text='inch')
    dpg = models.TextField(null=True, blank=True, )
    chip = models.TextField(null=True, blank=True, )
    gpu = models.TextField(null=True, blank=True, )
    ram = models.IntegerField(null=True, blank=True, default=None, help_text='GB')
    rom = models.IntegerField(null=True, blank=True, default=None, help_text='GB')
    sim_number = models.IntegerField(null=True, blank=True, default=None)
    weight = models.FloatField(null=True, blank=True, default=None, help_text='g')
    size_of_phone = models.TextField(null=True, blank=True,)
    bluetooth = models.CharField(
        max_length=10,
        choices=bluetooth_choice,
        default='Yes',
    )
    # class Meta:
    #     # proxy = True
    #     pass

# ---------------------------------------------------------------------------------------- #
class Clothes(Product):
    material = models.TextField( null=True, blank=True)
    origin = models.TextField( null=True, blank=True)
    brand = models.TextField( null=True, blank=True)
    size = models.CharField(null=True, blank=True, max_length=100)
    type = models.TextField( null=True, blank=True)
    
    # class Meta:
    #     # proxy = True
    #     pass

# ---------------------------------------------------------------------------------------- #
class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return f"{self.user} - {self.quantity} : {self.product.name} "
    
    def total_price(seft):
        return seft.product.price * seft.quantity

# ---------------------------------------------------------------------------------------- #
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    order = models.ManyToManyField(OrderProduct, blank=True)
   
    def total_price(self):
        total = 0
        for order in self.order:
            total += order.total_price()
        return total

    def __str__(self):
        return f"Cart of {self.user}"