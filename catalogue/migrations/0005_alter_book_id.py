# Generated by Django 4.2.5 on 2023-09-17 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
