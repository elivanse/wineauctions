# Generated by Django 4.1.dev20211210161305 on 2022-01-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('cf', 'Cabernet Franc'), ('pn', 'Pinot Noir'), ('cd', 'Chardonnay'), ('mc', 'Malbec'), ('mt', 'Merlot'), ('sh', 'Shiraz'), ('sy', 'Syrah'), ('pb', 'Pinot Blanc'), ('sb', 'Sauvignon Blanc'), ('cs', 'Cabernet Sauvignon')], max_length=67),
        ),
    ]
