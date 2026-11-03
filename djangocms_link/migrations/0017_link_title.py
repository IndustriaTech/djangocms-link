from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_link', '0016_alter_link_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(
                blank=True,
                help_text='Shown as the link\'s title attribute. If empty, "Learn more about <page title>" is used for internal links, "Go to external link" for external links, "Call <phone>" for phone links and "Write to <email>" for email links.',
                max_length=250,
                null=True,
                verbose_name='Link title',
            ),
        ),
    ]
