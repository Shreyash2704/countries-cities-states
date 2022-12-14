# Generated by Django 4.0.3 on 2022-08-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('state_id', models.IntegerField()),
                ('state_code', models.CharField(max_length=255)),
                ('state_name', models.CharField(max_length=255)),
                ('country_id', models.IntegerField()),
                ('country_code', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('wikiDataId', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('iso3', models.CharField(max_length=255)),
                ('iso2', models.CharField(max_length=255)),
                ('numeric_code', models.CharField(max_length=255)),
                ('phone_code', models.CharField(max_length=255)),
                ('capital', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('currency_name', models.CharField(max_length=255)),
                ('currency_symbol', models.CharField(max_length=255)),
                ('tld', models.CharField(max_length=255)),
                ('native', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('subregion', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('emoji', models.CharField(max_length=255)),
                ('emojiU', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('country_id', models.IntegerField()),
                ('country_code', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=255)),
                ('state_code', models.CharField(max_length=255)),
                ('latitute', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
            ],
        ),
    ]
