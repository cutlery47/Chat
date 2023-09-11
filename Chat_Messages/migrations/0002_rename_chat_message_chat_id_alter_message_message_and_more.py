# Generated by Django 4.2.4 on 2023-09-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat_Messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chat',
            new_name='chat_id',
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_first_name',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_last_name',
            field=models.CharField(blank=True),
        ),
    ]
