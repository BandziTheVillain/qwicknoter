from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    def snippet(self):
        if self.text:
            if len(self.text) > 50:
                return self.text[:50] + "..." 
            else:
                return self.text
        else:
            return None
    