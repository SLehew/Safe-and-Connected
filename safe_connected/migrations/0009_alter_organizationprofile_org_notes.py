# Generated by Django 4.2.3 on 2023-07-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0008_organizationprofile_org_notes_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationprofile',
            name='org_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
