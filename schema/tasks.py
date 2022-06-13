
import csv
import datetime
from celery import shared_task
from faker import Faker
from schema.models import Dataset, Schema, Column
from fakery.settings import MEDIA_ROOT
from celery_progress.backend import ProgressRecorder


faker = Faker()


@shared_task(bind=True)
def create_set(self, schema_id, row_count, filepath, dataset_id):
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        progress_recorder.set_progress(i + 1, 5, f'Row {i}')

    obj = {"name": Faker().name()}
    schema_id = schema_id
    row_count = row_count
    columns = Column.objects.filter(schema_id=schema_id).order_by("order")
    column_names = columns.values_list("clm_name", flat=True)
    with open(filepath, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(column_names)

        for _ in range(row_count):
            row = []
            for column in columns:
                obj = {
                    "name": faker.name(),
                    "job": faker.job(),
                    "email": faker.email(),
                    "address": faker.address(),
                    "phone": faker.phone_number(),
                    "domain": faker.domain_name(),
                    "company": faker.company(),
                    "text": faker.text(),
                    "integer": faker.random_int(
                        column.range_from,
                        column.range_to) if column.range_to and column.range_from else faker.random_int(),
                    "date": faker.date(),
                }
                row.append(obj[column.field_type])
            writer.writerow(row)
    Dataset.objects.filter(id=dataset_id).update(status="Done")
    return ''
