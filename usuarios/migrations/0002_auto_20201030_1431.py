# Generated by Django 3.1.2 on 2020-10-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gerente',
        ),
        migrations.RemoveField(
            model_name='empledo',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='empledo',
            name='edad',
        ),
        migrations.AddField(
            model_name='empledo',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]