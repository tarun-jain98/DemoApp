from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

# Register your models here.

admin.site.site_header = "Assignment System";

class UserResource(resources.ModelResource):
	class Meta:
		model = User

@admin.register(User)
class UserAdmin(DjangoUserAdmin, ImportExportModelAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone',)}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   )}),

		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
	search_fields = ('email', 'first_name', 'last_name', 'username', 'phone')
	ordering = ('username',)
	read_only = "password"
	resource_class = UserResource




