from django.contrib import admin
from .models import Query


class QueryAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'email',
    )

    ordering = ('created_on',)

admin.site.register(Query, QueryAdmin)