# Generated by Django 2.1.5 on 2019-02-11 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendario', '0002_auto_20190211_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]