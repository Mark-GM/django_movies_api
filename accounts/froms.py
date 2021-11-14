from django.contrib.auth.forms import UserChangeForm
from django.forms import fields

class UserAdminForm(UserChangeForm):
    class Meta:
        fields = "__all__"