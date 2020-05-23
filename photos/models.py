from django.db import models
import datetime as dt

# Create your models here.
        
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =60)
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length =100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_image(self):
        self.update()        

    @classmethod
    def get_image_by_id(cls):
        image = cls.objects.filter(id)
        return image
    
    @classmethod
    def filter_by_location(cls,location):
        location = cls.objects.filter(location)
        return location     
    
    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return news 
    class Meta:
        ordering = ['title']  