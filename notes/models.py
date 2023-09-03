from django.db import models
from user.models import CustomUser
from django.conf import settings
from django.utils.text import slugify

class Notes(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user_notes")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=50,blank=True,null=True, unique=True, db_index=True)
    title = models.CharField(max_length =100)
    subject = models.CharField(max_length=30)
    university = models.CharField(max_length=30,blank=True, null=True)
    notesfile = models.FileField()
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=10000, null=True)
    tags = models.CharField(max_length=30,blank=True, null=True)
    upvotes =models.ManyToManyField(CustomUser, related_name="votes" )
        
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Notes.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        self.slug=unique_slug[:50]
        super().save(*args,**kwargs)

    def get_note_slug(self):
        print(self.slug)
        return self.slug


    @property
    def total_upvotes(self):
        return self.upvotes.count()
    
    @property
    def excerpt(self):
       return self.description[:100] + '...'

class Comments(models.Model):
    comment=models.CharField(max_length=100)
    author_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    note=models.ForeignKey(Notes, on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)
    class Meta:
        ordering = ('date',)