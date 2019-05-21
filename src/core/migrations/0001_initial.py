# Generated by Django 2.2.1 on 2019-05-21 12:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HSCodeCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='HSCodeSubcategory',
            fields=[
                ('subcategory_name', models.CharField(max_length=120)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hs_code_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.HSCodeCategory')),
            ],
        ),
        migrations.CreateModel(
            name='HSCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=120)),
                ('short_description', models.CharField(max_length=120)),
                ('hs_code_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.HSCodeSubcategory')),
            ],
        ),
    ]
