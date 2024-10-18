# Generated by Django 5.1.2 on 2024-10-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('p', 'Pending'), ('w', 'working'), ('d', 'Done')], default='p', max_length=1)),
                ('creation_date', models.DateField()),
            ],
        ),
    ]
