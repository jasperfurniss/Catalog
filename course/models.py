from django.db import models

from filer.fields.image import FilerImageField


DURATION = (
    ('2', '2 Weeks'),
    ('8', '8 Weeks'),
)


class Course(models.Model):
    course_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    instructor = models.CharField(max_length=255, null=True, blank=True)
    course_duration = models.CharField(max_length=25, choices=DURATION, default=DURATION[0][0])
    art = FilerImageField(null=True, blank=True)

    def __unicode__(self):
        return u'{}'.format(self.name)

