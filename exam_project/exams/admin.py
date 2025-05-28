from django.contrib import admin
from .models import abexam

class abexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'exam_date', 'is_public')
    list_filter = ('is_public', 'created_date')
    search_fields = ('title', 'users__email')
    filter_horizontal = ('users',)
    date_hierarchy = 'exam_date'

admin.site.register(abexam, abexamAdmin)