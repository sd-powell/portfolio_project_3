from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Genre choices
GENRE_CHOICES = [(g, g) for g in [
    'House', 'Techno', 'Disco', 'Jazz', 'Rock', 'Funk',
    'Hip-Hop', 'Ambient', 'Drum and Bass', 'Soul', 'Classical',
    'Reggae', 'Trance', 'Electro', 'Synth-pop', 'Dubstep'
]]

# Rating choices for star display
RATING_CHOICES = [(i, f"{i} Stars") for i in range(1, 6)]

# Camelot Wheel keys for music
CAMELOT_KEYS = [
    ('1A', '1A - Ab Minor'),   ('1B', '1B - B Major'),
    ('2A', '2A - Eb Minor'),   ('2B', '2B - F# Major'),
    ('3A', '3A - Bb Minor'),   ('3B', '3B - D# Major'),
    ('4A', '4A - F Minor'),    ('4B', '4B - A# Major'),
    ('5A', '5A - C Minor'),    ('5B', '5B - D Major'),
    ('6A', '6A - G Minor'),    ('6B', '6B - B Major'),
    ('7A', '7A - D Minor'),    ('7B', '7B - F Major'),
    ('8A', '8A - A Minor'),    ('8B', '8B - C Major'),
    ('9A', '9A - E Minor'),    ('9B', '9B - G Major'),
    ('10A', '10A - B Minor'),  ('10B', '10B - D Major'),
    ('11A', '11A - F# Minor'), ('11B', '11B - A Major'),
    ('12A', '12A - Db Minor'), ('12B', '12B - E Major'),
]

YEAR_VALIDATORS = [MinValueValidator(1000), MaxValueValidator(9999)]
BPM_VALIDATORS = [MinValueValidator(24), MaxValueValidator(1000)]

DEFAULT_COVER_URL = (
    "https://res.cloudinary.com/dfavq8q6t/image/upload/"
    "v1747928584/default-cover_ffbxw4.webp"
)


class Record(models.Model):
    """
    A model representing a single vinyl record in a user's collection.

    Includes metadata such as title, artist, release year, genre, BPM,
    musical key (Camelot notation), cover image, and personal rating.
    Each record is linked to a user and timestamps are recorded for
    creation and last modification.

    A boolean field indicates if the record is a staff pick
    for homepage display.

    Automatically generates a URL-friendly slug from the title and artist.
    If no cover image is uploaded, a default image is assigned on save.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=YEAR_VALIDATORS,
        help_text="Enter a 4-digit year (e.g. 1982)"
    )
    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,
        blank=True,
        help_text="Select a genre"
    )
    cover_image = CloudinaryField('image', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        blank=True,
        null=True,
        help_text="Rate this record from 1 (worst) to 5 (best)"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    is_staff_pick = models.BooleanField(
        default=False,
        help_text="Tick to feature this record on the homepage as a staff pick"
    )

    slug = models.SlugField(blank=True, max_length=255, unique=True)

    def save(self, *args, **kwargs):
        """
        Override the default save method to:

        1. Automatically generate a unique slug based on the
        record's title and artist.
        - Slug is created using Django’s `slugify()` utility.
        - If a slug conflict is detected
        (i.e., already exists in the database),
            a numeric suffix (e.g., -1, -2) is appended until
            uniqueness is achieved.
        - This avoids clashes and ensures stable, human-readable URLs.

        2. Assign a default cover image if none is provided by the user.

        Calls the superclass `save()` method to persist the instance.
        """
        if not self.slug:
            base_slug = slugify(f"{self.title}-{self.artist}")
            slug = base_slug
            num = 1
            while Record.objects.filter(slug=slug).exclude(
                pk=self.pk
            ).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug

        if not self.cover_image:
            self.cover_image = DEFAULT_COVER_URL

        super().save(*args, **kwargs)

        class Meta:
            ordering = ["title"]

        def __str__(self):
            return f"{self.title} by {self.artist}"


class Track(models.Model):
    """
    A model representing a single track on a vinyl record.

    Each track is linked to a specific record and includes metadata
    such as title, artist, BPM, and musical key (Camelot notation).
    """
    record = models.ForeignKey(
        Record, on_delete=models.CASCADE, related_name="tracks"
        )
    title = models.CharField(max_length=255)
    position = models.CharField(
        max_length=5,
        blank=True,
        help_text="Enter track position (e.g. A1, B2)",
        db_index=True
    )
    duration = models.CharField(
        max_length=10,
        blank=True,
        help_text="Enter track duration (e.g. 3:45)"
    )
    bpm = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=BPM_VALIDATORS,
        help_text="Enter BPM between 24 and 1000"
    )
    key = models.CharField(
        max_length=4,
        choices=CAMELOT_KEYS,
        blank=True,
        help_text="Select a key using Camelot notation"
    )

    class Meta:
        ordering = ['position', 'title']

    def __str__(self):
        return f"{self.position or ''} {self.title}"
