# Generated by Django 3.2.5 on 2021-07-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClothes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('weather', models.CharField(choices=[('맑음', '맑음'), ('흐림', '흐림'), ('비', '비'), ('눈', '눈')], default='', max_length=20)),
                ('temperature', models.IntegerField(default=0)),
                ('post_date', models.DateField()),
            ],
            options={
                'db_table': 'MyClothes',
            },
        ),
    ]
