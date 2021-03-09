from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PostQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            if obj.img.name.split('/')[-1] != 'default.jpg':
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

    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(id=self.id)
            if (this.img != self.img) and (this.img.name.split('/')[-1] != 'default.jpg'):
                this.img.delete(save=False)
        except: pass
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})