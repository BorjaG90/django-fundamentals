from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Invitation(models.Model):
  from_user = models.ForeignKey(User, on_delete="cascade", related_name="invitations_sent")
  to_user = models.ForeignKey(User, on_delete="cascade", related_name="invitations_received")
  message = models.CharField(max_length=300)
  timestamp = models.DateTimeField(auto_now_add=True)