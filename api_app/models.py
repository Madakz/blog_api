from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.SlugField(blank = True, max_length = 200, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return  self.title
    

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1
        #when slug exist add 1 to the integer value of the existig slug
        while Blog.objects.filter(slug = slug).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        self.slug = slug

        super().save(*args, **kwargs)  # This ensures the record is saved to the database