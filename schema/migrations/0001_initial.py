# Generated by Django 4.0.5 on 2022-06-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('field_type', models.CharField(choices=[('name', 'name'), ('job', 'job'), ('email', 'email'), ('domain', 'domain'), ('phone', 'phone'), ('company', 'company'), ('address', 'address'), ('date', 'date'), ('integer', 'integer'), ('text', 'text')], default='text', max_length=15)),
                ('range_from', models.IntegerField(blank=True, null=True)),
                ('range_to', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.schema')),
            ],
        ),
    ]