# Generated by Django 4.2.7 on 2024-02-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_alter_issuedbook_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(max_length=13),
        ),
    ]