from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.




#admin.site.register(Post,ItemAdmin)
@admin.register(Post)
class PostImportExport(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
    list_filter = ['active', 'category']
    search_fields = ['active', 'category']

#admin.site.register(Category)
@admin.register(Category)
class PostImportExport(ImportExportModelAdmin):
    pass