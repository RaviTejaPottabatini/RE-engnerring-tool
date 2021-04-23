# Generated by Django 3.0.6 on 2020-06-09 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceInfo',
            fields=[
                ('auto_project_id', models.AutoField(primary_key=True, serialize=False)),
                ('servicename', models.CharField(max_length=64)),
                ('communication_text', models.CharField(max_length=64)),
                ('things_text', models.CharField(max_length=64)),
                ('child', models.CharField(max_length=64)),
                ('parent', models.CharField(max_length=64)),
                ('direction', models.CharField(choices=[('horizantal', 'HORIZANTAL'), ('vertical', 'VERTICAL')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
