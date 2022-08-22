from django.db import models

# Create your models here.


class Post(models.Model):
    # owner = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )
    title        = models.CharField(max_length=100)
    post         = models.CharField(max_length=500)
    # thumbnail    = models.ImageField(upload_to='gallery_thumbs', blank = True, null = True)
    # is_public    = models.BooleanField( default=False)
    date_created = models.DateTimeField( verbose_name="date created", auto_now_add=True)
