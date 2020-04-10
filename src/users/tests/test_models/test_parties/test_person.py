from django.contrib.auth.models import (
    AbstractUser,
)
from django.test import (
    TestCase,
)

from users.models import (
    Person,
)


class PersonTestCase(TestCase):

    def test_type(self):
        self.assertTrue(issubclass(Person, AbstractUser))
