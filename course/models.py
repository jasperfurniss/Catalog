from django.db import models
from autoslug import AutoSlugField


DURATION = (
    ('2', '2 Weeks'),
    ('8', '8 Weeks'),
)


class Course(models.Model):
    course_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    instructor = models.CharField(max_length=255, null=True, blank=True)
    course_duration = models.CharField(max_length=25, choices=DURATION, default=DURATION[0][0])
    art = models.ImageField(upload_to="static/uploads")
    slug = AutoSlugField(populate_from='course_title')

    def __unicode__(self):
        return u'{}'.format(self.course_title)

