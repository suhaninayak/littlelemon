from django.db import models

# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000,default='')
    category = models.CharField(
    max_length=50, 
    choices=[
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('pizza', 'Pizza'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage')
    ], 
    default='main'  # <-- Add this default value
)

    def __str__(self):
        return self.name
    