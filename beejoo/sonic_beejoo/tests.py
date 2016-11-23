from django.test import TestCase
from sonic_beejoo.models import DesignType
# Create your tests here.


class TestDesignType(TestCase):
    def test_design_create(self):
        design = DesignType.objects.create(name='test_design')
        assert design.pk is not None