from django.db import models
import uuid
# Create your models here.


class Profile(models.Model):
    email = models.EmailField()
    token = models.CharField(default='', max_length=1000)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.token = str(uuid.uuid4())
        super(Profile, self).save(*args, **kwargs)
