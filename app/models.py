from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta():
        db_table = 'tb_Category'

        def __str__(self):
            return self.name
            
class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default="NULL")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta():
        db_table = 'tb_Blog'

        def __str__(self):
            return self.name
            return self.content