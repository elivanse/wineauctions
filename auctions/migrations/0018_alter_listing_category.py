# Generated by Django 4.1.dev20211210161305 on 2021-12-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('cf', 'Cabernet Franc'), ('cs', 'Cabernet Sauvignon'), ('cd', 'Chardonnay'), ('mc', 'Malbec'), ('sh', 'Shiraz'), ('sy', 'Syrah'), ('pb', 'Pinot Blanc'), ('sb', 'Sauvignon Blanc'), ('mt', 'Merlot'), ('pn', 'Pinot Noir')], max_length=67),
        ),
    ]
