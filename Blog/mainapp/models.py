from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    article = models.TextField()
    create_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
       return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    comment=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name






    


