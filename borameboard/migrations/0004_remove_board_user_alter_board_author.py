# Generated by Django 4.1.4 on 2023-03-17 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('borameboard', '0003_board_user_alter_board_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.AlterField(
            model_name='board',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]