# Generated by Django 3.2.6 on 2021-09-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auction_lst_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_lst',
            name='category',
            field=models.CharField(choices=[('shoe', 'Shoes'), ('all', 'All categories'), ('fish', 'Fishing goods'), ('nt', 'Notebooks'), ('ant', 'Antiquities'), ('dt', 'Desktop Computer')], default={('shoe', 'Shoes'), ('all', 'All categories'), ('fish', 'Fishing goods'), ('nt', 'Notebooks'), ('ant', 'Antiquities'), ('dt', 'Desktop Computer')}, max_length=67),
        ),
    ]