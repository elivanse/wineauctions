# Generated by Django 4.1.dev20211210161305 on 2022-02-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0080_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sb', 'Sauvignon Blanc'), ('pn', 'Pinot Noir'), ('mt', 'Merlot'), ('pb', 'Pinot Blanc'), ('cf', 'Cabernet Franc'), ('cd', 'Chardonnay'), ('cs', 'Cabernet Sauvignon'), ('mc', 'Malbec'), ('sy', 'Syrah'), ('sh', 'Shiraz')], max_length=67),
        ),
    ]
