from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("records", "0002_record_is_staff_pick"),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
