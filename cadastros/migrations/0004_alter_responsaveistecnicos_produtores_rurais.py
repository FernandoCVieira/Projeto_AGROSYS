# Generated by Django 4.2.1 on 2023-05-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_produtorrural_responsaveis_tecnicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsaveistecnicos',
            name='produtores_rurais',
            field=models.ManyToManyField(blank=True, null=True, to='cadastros.produtorrural', verbose_name='Produtor Rural'),
        ),
    ]