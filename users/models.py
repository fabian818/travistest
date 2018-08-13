
import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    optional_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, unique=True)
    class Meta:
        managed = True
        db_table = 'users'
        unique_together = (('email', 'optional_id'),)