from django.db import models

# Create your models here.
class Roster(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(models.User)

    title = models.CharField(max_length=255)
    employees = models.ListField(models.ForeignKey(User))

class WorkEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(models.User)

    description = models.TextField()
    datetime = models.DateTimeField()
