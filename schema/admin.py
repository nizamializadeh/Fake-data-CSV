from django.contrib import admin

from schema.models import Column, Schema, Dataset

admin.site.register(Schema)
admin.site.register(Column)
admin.site.register(Dataset)
