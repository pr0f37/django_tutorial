import datetime

from django.test import TestCase

from django.utils import timezone
from .models import Post

class PostMethodTest(TestCase):
    def testWasPublishedRecentlyWithFutureDate(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertEqual(future_post.wasPublishedRecently(), False)
