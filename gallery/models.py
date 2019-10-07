from django.db import models

# Create your models here.
class Category (models.Model):
    category = models.CharField(max_length =30)
    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()
        
class Location (models.Model):
    location = models.CharField(max_length =30)
    
    def __str__(self):
        return self.location
    
    class Meta:
        ordering = ['location']
        
    def save_location(self):
        self.save()
        
class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='DEFAULT VALUE')
    image_name =models.CharField(max_length =60) 
    image_description = models.CharField(max_length=255)
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE,)
    image_category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    

