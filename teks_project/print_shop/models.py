from django.db import models
from django.utils import timezone
from django.urls import reverse

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('print_shop:service_detail', kwargs={'slug': self.slug})

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.company}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('print_shop:post_detail', kwargs={'slug': self.slug})

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Contact from {self.name} on {self.created_date.strftime('%Y-%m-%d')}"
