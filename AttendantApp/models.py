from django.db import models
from django.core.urlresolvers import reverse

from djangotoolbox.fields import ListField, EmbeddedModelField

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        ordering = ["-created_at"]

class Roster(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(User)

    title = models.CharField(max_length=255)
    employees = ListField(models.ForeignKey(User))

class WorkEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(User)

    description = models.TextField()
    datetime = models.DateTimeField()
