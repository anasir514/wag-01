# Generated by Django 3.1.7 on 2021-02-19 21:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0007_genericpage_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], null=True),
        ),
    ]
