# Generated by Django 3.2.3 on 2021-05-26 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0002_question_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('0', 'Passive'), ('1', 'Active')], default=0, max_length=1),
        ),
    ]
