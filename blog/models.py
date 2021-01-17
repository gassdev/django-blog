from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PostQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            obj.img.delete()
        super(PostQuerySet, self).delete(*args, **kwargs)

class Post(models.Model):
    objects = PostQuerySet.as_manager()
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    img = models.ImageField(default='default.jpg', upload_to='post/images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.img.name.split('/')[-1] != 'default.jpg':
            self.img.delete()
        super().delete(*args, **kwargs)  # Call the "real" save() method.
