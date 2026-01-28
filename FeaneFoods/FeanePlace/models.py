from django.db import models
from django.forms import ModelForm
# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}" 

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}" 

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Burger, Pizza, Pasta, etc.
    slug = models.SlugField(max_length=50, unique=True)  # for CSS classes or URLs
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    description = models.TextField()        
    image = models.ImageField(upload_to='menu_images/')  # will need MEDIA setup
    is_available = models.BooleanField(default=True)  # optional: hide items when out of stock
    def __str__(self):
        return self.name    

