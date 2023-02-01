from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Item(models.Model):
    Item_id = models.CharField(max_length=10, primary_key=True)
    Item_name = models.CharField(max_length=30)
    Stock = models.IntegerField()
    Item_desc = models.TextField(null= True)
    To_use_video  =  models.FileField(upload_to='{%  static "videos/" %}',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    Item_desc_video = models.FileField(upload_to='{%  static "videos/" %}',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

class Item_variation(models.Model):
    Variation_id = models.ForeignKey(Item , on_delete = models.CASCADE)
    Variation_name = models.CharField(max_length = 20)
    img1 = models.ImageField(upload_to="{% static 'images/' %}",null = True)
    img2 = models.ImageField(upload_to="{% static 'images/' %}",null = True)
    img3 = models.ImageField(upload_to="{% static 'images/' %}",null = True)
    img4 = models.ImageField(upload_to="{% static 'images/' %}",null = True)
    img5 = models.ImageField(upload_to="{% static 'images/' %}",null = True)
    img6 = models.ImageField(upload_to="{% static 'images/' %}",null = True)
    img7 = models.ImageField(upload_to="{% static 'images/' %}",null = True)
    img8 = models.ImageField(upload_to="{% static 'images/' %}",null = True)

    
