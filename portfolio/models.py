from django.db import models
from django.core.files.storage import FileSystemStorage

press_release_storage = FileSystemStorage()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    file = models.FileField(
        upload_to='files',
        storage=press_release_storage,
        blank=True, null=True
    )


    def __str__(self):
        return self.title



    
