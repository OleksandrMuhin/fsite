from audioop import reverse

from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=10, blank='False')
    photo = models.ImageField(upload_to='images/')
    url = models.URLField(blank='False')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Trenings(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank='False')
    title = models.CharField(max_length=10)
    img = models.ImageField(upload_to='images/')
    desc = models.TextField()


class Socials(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank='False')
    title = models.CharField(max_length=15, blank='False')
    icon = models.ImageField()
    url = models.URLField()


class Blogs(models.Model):
    title = models.CharField(max_length=15, blank='False')
    blog_title = models.CharField(max_length=40, blank='False')
    blog_text = models.TextField(blank='False')
    blog_img = models.ImageField(upload_to='images/')
    blog_url = models.URLField(blank='False')
    blog_read_time = models.CharField(max_length=20, blank='False')


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_blog', kwargs={'blog_id':self.pk})


