# Generated by Django 3.2 on 2021-04-22 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='watering',
            name='date',
            field=models.DateField(verbose_name='Watering Date'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
        ),
    ]
