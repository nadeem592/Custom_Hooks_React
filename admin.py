from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import NiftyModel

# Register your models here.
@admin.register(NiftyModel)
class UserData(ImportExportModelAdmin):
    pass
