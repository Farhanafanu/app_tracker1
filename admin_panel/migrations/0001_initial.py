# Generated by Django 4.2.5 on 2024-08-22 06:55

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
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('points', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='screenshots/')),
                ('completed', models.BooleanField(default=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.app')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_usertasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
