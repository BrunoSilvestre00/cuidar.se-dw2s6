# Generated by Django 4.1.3 on 2022-12-15 01:36

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
            name='Anotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Valor')),
                ('datetime', models.DateTimeField(verbose_name='Data e hora')),
                ('observation', models.CharField(max_length=255, verbose_name='Observações')),
                ('category', models.CharField(choices=[('DIABETES', 'Diabetes'), ('TEMPERATURE', 'Temperatura'), ('PRESSURE', 'Pressão'), ('HEART_BEAT', 'Batimento Cardíaco'), ('WEIGHT', 'Peso'), ('MEDICATION', 'Medicação'), ('OXYGENATION', 'Oxygenação'), ('MOOD', 'Humor'), ('SORENESS', 'Dor')], max_length=20)),
                ('status', models.CharField(choices=[('VERY_UNSTABLE', 'Muito instável'), ('UNSTABLE', 'Instável'), ('MODERATE', 'Razoável'), ('STABLE', 'Estável')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Anotação',
                'verbose_name_plural': 'Anotações',
                'db_table': 'annotations',
            },
        ),
    ]
