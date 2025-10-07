from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from . validators import validate_file_size

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    summary = models.TextField()
    body = RichTextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)[:50]
        super().save(*args, **kwargs)

    @property
    def slug_id(self):
        return f"{self.slug}-{self.id}"

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    dimensions = models.CharField(max_length=30)
    scale = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)
        
    @property
    def slug_id(self):
        return f"{self.slug}-{self.id}"

    def __str__(self):
        return self.title
    
    

class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='content/images', validators=[validate_file_size])
        
    
        