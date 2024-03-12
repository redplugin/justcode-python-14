# Generated by Django 4.2 on 2024-02-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['title', 'content'], name='posts_title_c84406_idx'),
        ),
    ]
