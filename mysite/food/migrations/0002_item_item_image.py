# Generated by Django 4.2.7 on 2023-11-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKGQK5GvJ24v4tkOAVrNDVUrdJMyCo_FgvRk2lWyjdjA&s', max_length=500),
        ),
    ]