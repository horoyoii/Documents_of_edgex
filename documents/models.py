from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    number = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, help_text="Slug will be generated automatically from the title of the post")    
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self):
        #self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title
