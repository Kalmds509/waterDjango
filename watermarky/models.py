from django.db import models
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



# Create your models here.
class Imaj(models.Model):
   
    pseudo = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="media/")
    
   
       
    class Meta:
        verbose_name='Imaj'
        verbose_name_plural='Imaj yo'

    def __str__(self):
        return self.pseudo

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        photo = Image.open(self.photo.path)
        draw = ImageDraw.Draw(photo)
        font = ImageFont.load_default()
        width, height = photo.size
       
        myword = "Code9Class !"
        margin = 10
        textwidth, textheight = draw.textsize(myword, font)
       
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x,y), myword, (255, 255, 255), font=font)
        photo.save(self.photo.path)

#     image = Image.open('image.jpg')
# watermark = Image.open('watermark.png')
# image.paste(watermark, (x, y), watermark)
