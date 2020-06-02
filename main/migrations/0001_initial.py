# Generated by Django 3.0.5 on 2020-05-25 18:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Duyurular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duyurular_title', models.CharField(max_length=200)),
                ('duyurular_content', models.TextField()),
                ('duyurular_published', models.DateTimeField(default=datetime.datetime(2020, 5, 25, 18, 30, 37, 653660, tzinfo=utc), verbose_name='Yayınlandığı Tarih')),
            ],
            options={
                'verbose_name_plural': 'Duyurular',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_last', models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 25, 18, 30, 37, 653991, tzinfo=utc))),
                ('login_count', models.CharField(blank=True, default='', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(default=1, max_length=255)),
                ('email_validated', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]