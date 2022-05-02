# Generated by Django 4.0.4 on 2022-05-01 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
            ],
            options={
                'verbose_name': 'reply',
                'verbose_name_plural': 'replies',
                'db_table': 'reply',
            },
        ),
    ]
