"""
Admin for accounts app
"""

from django.contrib import admin

from authtools.admin import UserAdmin as UserAdminBase
from hijack.admin import HijackUserAdminMixin

from .models import User


class UserAdmin(HijackUserAdminMixin, UserAdminBase):
    """
    User admin. Extends from authtools' admin.
    """

    list_display = UserAdminBase.list_display + ('hijack_field',)

admin.site.register(User, UserAdmin)

