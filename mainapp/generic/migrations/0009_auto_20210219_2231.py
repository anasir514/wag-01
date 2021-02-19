# Generated by Django 3.1.7 on 2021-02-19 22:31

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0008_genericpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(template='heading_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], null=True),
        ),
    ]
