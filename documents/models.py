from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_documents')
    shared_with = models.ManyToManyField(User, related_name='shared_documents', blank=True)
    class Meta:
        app_label = 'documents'

class Access(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=False)