# Generated by Django 4.2 on 2024-02-24 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'content')},
        ),
    ]
