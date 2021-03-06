# Generated by Django 3.2.5 on 2021-07-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('all', '全員'), ('limited', '会員限定')], max_length=50)),
            ],
        ),
    ]
