from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField




class Course(models.Model):
    course_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    instructor = models.CharField(max_length=255, null=True, blank=True)
    course_duration = models.CharField(max_length=255, null=True, blank=True)
    art = models.CharField(max_length=255, null=True, blank=True)


    def __unicode__(self):
        return u'{}'.format(self.name)
