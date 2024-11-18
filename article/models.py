from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext as _
import readtime

STATUS = (
    (
        ('Pending', 'Pending'),
        ('Approve', 'Approve'),
        ('Reject', 'Reject'),
    )
)

class MainArticle(models.Model):
    id = models.AutoField(primary_key=True)
    bigTitle = models.CharField(_("BIG TITLE"), max_length=10)
    headline = models.CharField(_("HEADER"), max_length=200)
    image = models.FileField(_("GAMBAR"), upload_to='images/%y', blank=True, null=True, default='../static/images/DabestCard.jpg')
    textarea = CKEditor5Field('DESKRIPSI', config_name='extends')
    createAt = models.DateTimeField(auto_now_add=True)
    author = models.CharField(_("AUTHOR"), max_length=50)

    def get_readtime(self):
      result = readtime.of_text(self.textarea)
      return result.text 

    def __str__(self):
      return self.bigTitle

class Tag(models.Model):
    nameTag = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nameTag

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(_("HEADER"), max_length=250)
    image = models.FileField(_("GAMBAR"), upload_to='images/%y', blank=True, null=True, default='../static/images/DabestCard.jpg')
    textarea = CKEditor5Field('DESKRIPSI', config_name='extends')
    createAt = models.DateTimeField(auto_now_add=True)
    author = models.CharField(_("AUTHOR"), max_length=50, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags')
    last_modified = models.DateTimeField(auto_now=True)
    artstatus = models.CharField(max_length=50, choices=STATUS, default='Pending')

    class Meta:
        ordering = ['-createAt']
        
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        
class ApprovedArticle(Article):
    class Meta:
        proxy = True
        verbose_name = _("  Approve Article")

class RejectArticle(Article):
    class Meta:
        proxy = True
        verbose_name = _("  Reject Article")

class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(_("HEADER"), max_length=250)
    image = models.FileField(_("GAMBAR"), upload_to='images/%y', blank=True, null=True, default='../static/images/DabestCard.jpg')
    textarea = CKEditor5Field('DESKRIPSI', config_name='extends')
    createAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createAt']

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.article}'"