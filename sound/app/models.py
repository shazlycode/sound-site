from django.db import models

# Create your models here.

class Baset(models.Model):
    player=models.CharField(max_length=100, default='')
    title= models.CharField(max_length=100, verbose_name="اسم السورة")
    # source=models.FileField(upload_to='sound',default='non.mp3' )
    path=models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.title
    
    
class Radio(models.Model):
    title= models.CharField(max_length=100)
    path= models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Menshawy(models.Model):
    player=models.CharField(max_length=100, default='محمد صديق المنشاوي')
    title= models.CharField(max_length=100)
    path= models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Husary(models.Model):
    player=models.CharField(max_length=100, default='محمود خليل الحصري')
    title= models.CharField(max_length=100)
    path= models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Bana(models.Model):
    player=models.CharField(max_length=100, default='محمود علي البنا')
    title= models.CharField(max_length=100)
    path= models.CharField(max_length=100)
    
    def __str__(self):
        return self.title