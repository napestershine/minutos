# Generated by Django 4.0.1 on 2022-02-01 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('INVITED', 'Invited'), ('ACCEPTED', 'Accepted')], default='INVITED', max_length=20)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='team.team')),
            ],
        ),
    ]
