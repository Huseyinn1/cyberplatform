# Generated by Django 5.1.6 on 2025-03-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Blog adını yazınız', max_length=200, unique=True, verbose_name='Blog adı')),
                ('image', models.ImageField(default='blogs/default.jpg', upload_to='blogs/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, null=True)),
                ('blog_url', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
