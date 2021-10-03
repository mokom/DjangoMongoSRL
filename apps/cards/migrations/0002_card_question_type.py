# Generated by Django 3.2.7 on 2021-10-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='question_type',
            field=models.IntegerField(choices=[(1, 'Mcqs'), (2, 'Fill In Blank'), (3, 'True Or False'), (4, 'Short Answer')], default=1),
        ),
    ]
