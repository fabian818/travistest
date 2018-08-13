# Generated by Django 2.1 on 2018-08-13 06:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('optional_id', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email', 'optional_id')},
        ),
    ]
