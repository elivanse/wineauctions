# Generated by Django 4.0.2 on 2022-02-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0072_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('cf', 'Cabernet Franc'), ('mc', 'Malbec'), ('pn', 'Pinot Noir'), ('cd', 'Chardonnay'), ('cs', 'Cabernet Sauvignon'), ('sb', 'Sauvignon Blanc'), ('sh', 'Shiraz'), ('sy', 'Syrah'), ('pb', 'Pinot Blanc'), ('mt', 'Merlot')], max_length=67),
        ),
    ]