# Generated by Django 4.0.6 on 2022-07-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todolistmodel_options_todolistmodel_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolistmodel',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='task',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]