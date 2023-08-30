from django.test import TestCase


class Testviews(TestCase):
    """Test the views"""

    def test_home_page(self):
        """Test the home page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
