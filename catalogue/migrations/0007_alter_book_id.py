# Generated by Django 4.2.5 on 2023-09-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_alter_author_id_alter_genre_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]