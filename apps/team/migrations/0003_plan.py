# Generated by Django 4.0.1 on 2022-02-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_invitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('max_projects_per_team', models.IntegerField(default=0)),
                ('max_members_per_team', models.IntegerField(default=0)),
                ('max_tasks_per_project', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
    ]