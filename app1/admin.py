from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from app1.models import Jtweet
from app1.forms import JtweetUserChangeForm, JtweetUserCreationForm

# Register your models here.


class JtweetUserAdmin(UserAdmin):

    form = JtweetUserChangeForm
    add_form = JtweetUserCreationForm
    #filter_horizontal = UserAdmin.filter_horizontal + ('followings',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Jtweet fields'), {'fields': ('followings',)}),
    )


class JtweetAdmin(admin.ModelAdmin):
    # pass
    list_display = ('text', 'owner')
    search_fields = ('text',)

admin.site.register(get_user_model(), JtweetUserAdmin)
admin.site.register(Jtweet, JtweetAdmin)