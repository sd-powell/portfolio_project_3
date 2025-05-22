from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Record = apps.get_model('records', 'Record')
    for record in Record.objects.all():
        base_slug = slugify(f"{record.title}-{record.artist}")
        slug = base_slug
        counter = 1
        while Record.objects.filter(slug=slug).exclude(id=record.id).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        record.slug = slug
        record.save()


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0003_record_slug"),
    ]

    operations = [
        migrations.RunPython(populate_slugs),
        migrations.AlterField(
            model_name='record',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
