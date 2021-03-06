# Generated by Django 4.1.dev20211210161305 on 2022-01-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0055_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sb', 'Sauvignon Blanc'), ('cs', 'Cabernet Sauvignon'), ('sy', 'Syrah'), ('cf', 'Cabernet Franc'), ('mc', 'Malbec'), ('mt', 'Merlot'), ('pb', 'Pinot Blanc'), ('cd', 'Chardonnay'), ('pn', 'Pinot Noir'), ('sh', 'Shiraz')], max_length=67),
        ),
    ]
