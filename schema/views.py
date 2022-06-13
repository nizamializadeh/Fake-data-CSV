from ast import Return
import os
from pickle import NONE
from unicodedata import name
from django.conf import settings
from django.shortcuts import redirect, render
from isort import file

from schema.models import Column, Dataset, Schema
from schema.tasks import create_set
from .forms import ColumnForm
from faker import Faker
import csv
import datetime
from django.http import HttpResponse
from fakery.settings import MEDIA_ROOT, MEDIA_URL

faker = Faker()


def index(request):
    context = {}
    context['schemas'] = Schema.objects.all()
    return render(request, "schema/index.html", context)


def create(request):
    context = {}
    context['form'] = ColumnForm()
    if request.method == 'POST':
        schemaname = request.POST['name']
        schema = Schema.objects.create(name=schemaname)
        clm_name = request.POST.getlist('clm_name')
        field_type = request.POST.getlist('field_type')
        range_from = request.POST.getlist(
            'range_from') if request.POST.getlist('range_from') else []
        range_to = request.POST.getlist(
            'range_to') if request.POST.getlist('range_to') else []
        order = request.POST.getlist('order')
 
        for clmn_count in range(len(clm_name)):
            Column.objects.create(
                schema=schema,
                clm_name=clm_name[clmn_count],
                field_type=field_type[clmn_count],
                range_from=range_from[clmn_count] if len(range_from) > 0 else None,
                range_to=range_to[clmn_count] if len(range_to) > 0 else None,
                order=order[clmn_count])

        return redirect('/schemas')
    return render(request, "schema/create.html", context=context)


def delete(request, pk):
    item = Schema.objects.get(pk=pk).delete()
    return redirect('index')


def create_dataset(request):
    context = {}

    if request.method == 'POST':
        schema_id = int(request.POST.get("schema_id"))
        row_count = int(request.POST.get("row_count"))
        schema = Schema.objects.filter(id=schema_id).first()
        filename = str(schema.name) + '_' + \
            str(datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
        filepath = f'{MEDIA_ROOT}\\{filename}'
        dataset = Dataset(
            schema_id=schema_id,
            file_name=filename,
            file_path=filepath,
            status='In progress'
        )
        dataset.save()
        result = create_set.delay(
            schema_id=schema_id,
            row_count=row_count,
            filepath=filepath,
            dataset_id=dataset.id)
        context['datasets'] = Dataset.objects.all()
        context['task_id'] = result.task_id

    return render(request, "dataset/index.html", context=context)


def index_dataset(request):
    context = {}
    context['datasets'] = Dataset.objects.all()
    return render(request, "dataset/index.html", context)
