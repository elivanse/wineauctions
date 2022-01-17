# Generated by Django 4.1.dev20211210161305 on 2022-01-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0038_alter_listing_category_alter_listing_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sy', 'Syrah'), ('cf', 'Cabernet Franc'), ('pn', 'Pinot Noir'), ('mc', 'Malbec'), ('cs', 'Cabernet Sauvignon'), ('mt', 'Merlot'), ('pb', 'Pinot Blanc'), ('sh', 'Shiraz'), ('cd', 'Chardonnay'), ('sb', 'Sauvignon Blanc')], max_length=67),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
    ]