"""
Models for accounts app
"""

from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    """
    user model. Inherits from authtools' user model
    """

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email



