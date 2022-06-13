from secrets import choice
from django.db import models
DEFAULT_CHOICE = "text"
CHOICES = (

    ('name', 'name'),
    ('job', 'job'),
    ('email', 'email'),
    ('domain', 'domain'),
    ('phone', 'phone'),
    ('company', 'company'),
    ('address', 'address'),
    ('date', 'date'),
    ('integer', 'integer'),
    ('text', 'text')

)


class Schema(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Column(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    clm_name = models.CharField(max_length=100, blank=False, null=False)
    field_type = models.CharField(
        default=DEFAULT_CHOICE,
        choices=CHOICES,
        max_length=15
    )
    range_from = models.IntegerField(blank=True, null=True)
    range_to = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clm_name


class Dataset(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=500, blank=False, null=False)
    file_path = models.CharField(max_length=500, blank=False, null=False)
    status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name
