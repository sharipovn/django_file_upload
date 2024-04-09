# file_upload/models.py

from django.db import models
from django.contrib.auth.models import User
import os

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    comment=models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    allowed_users = models.ManyToManyField(User, related_name='allowed_files', blank=True)
    

    def delete(self, *args, **kwargs):
        try:
            storage, path = self.file.storage, self.file.path
            if os.path.exists(path):
                storage.delete(path)
            super().delete(*args, **kwargs)
        except:
            print('Some errors occured')