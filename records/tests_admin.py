from django.test import TestCase, RequestFactory
from django.contrib.admin.sites import AdminSite
from records.admin import RecordAdmin
from records.models import Record, User


class MockCoverImage:
    """
    Mock object to simulate a cover image with a .url attribute.
    """
    url = 'https://example.com/test-image.jpg'


class RecordAdminTests(TestCase):
    """
    Unit tests for custom admin functionality in RecordAdmin.
    Focus on cover_thumb image rendering logic and edge cases.
    """

    def setUp(self):
        """
        Set up a test user and a RecordAdmin instance with a mock request.
        """
        self.factory = RequestFactory()
        self.site = AdminSite()
        self.admin = RecordAdmin(Record, self.site)
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def make_record(self, **kwargs):
        """
        Helper to create a minimal valid Record instance
        with optional overrides.
        """
        defaults = {
            'title': 'Test Record',
            'artist': 'Test Artist',
            'user': self.user,
            'genre': 'Electronic',
            'rating': 3,
        }
        defaults.update(kwargs)
        return Record.objects.create(**defaults)

    def test_cover_thumb_with_valid_image(self):
        """
        cover_thumb should return a valid <img> tag if a cover image exists.
        """
        record = self.make_record()
        record.cover_image = MockCoverImage()
        html = self.admin.cover_thumb(record)
        self.assertIn('<img src="https://example.com/test-image.jpg"', html)

    def test_cover_thumb_with_no_image(self):
        """
        cover_thumb should return "No image" if cover_image is None.
        """
        record = self.make_record()
        record.cover_image = None
        self.assertEqual(self.admin.cover_thumb(record), "No image")

    def test_cover_thumb_with_invalid_image(self):
        """
        cover_thumb should return "Invalid image"
        if accessing .url raises an error.
        """
        class BrokenImage:
            def __getattr__(self, name):
                raise Exception("Broken")

        record = self.make_record()
        record.cover_image = BrokenImage()
        self.assertEqual(self.admin.cover_thumb(record), "Invalid image")
