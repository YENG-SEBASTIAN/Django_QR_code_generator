from distutils.command.upload import upload
from django.db import models
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File


# Create your models here.

class QrGenerator(models.Model):
    name = models.CharField(max_length = 200)
    qr_code_img = models.ImageField(upload_to='qr_code_img', blank =True)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        qr_code_name = qrcode.make(self.name)
        qr_code_size = Image.new('RGB', (300, 300), 'white')
        draw_qr_code = ImageDraw.Draw(qr_code_size)
        qr_code_size.paste(qr_code_name)
        fname = 'QR_Code-{self.name}.png'
        buffer = BytesIO()
        qr_code_size.save(buffer, 'PNG')
        self.qr_code_img.save(fname, File(buffer), save=False)
        qr_code_size.close()
        super().save(*args, **kwargs)