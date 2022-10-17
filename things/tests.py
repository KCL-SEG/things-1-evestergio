from django.test import TestCase
from .models import Thing
from django.core.exceptions import ValidationError

class ThingModelTestCase(TestCase):
    def setUp(self):
        self.thing = Thing.objects.create_thing(
            name = 'Thing-1',
            description = 'This is the description for thing #1',
            quantity = 23,
        )

    def test_valid_thing(self):
        self._assert_thing_is_valid()

    #name tests
    def test_name_cannot_be_blank(self):
        self.thing.name=''
        self._assert_thing_is_invalid()

    def test_name_can_be_30_characters_long(self):
        self.thing.name= 'x' * 30
        self._assert_thing_is_valid()

    def test_name_cannot_be_over_30_characters_long(self):
        self.thing.name= 'x' * 31
        self._assert_thing_is_invalid()

    def test_name_must_be_unique(self):
        second_thing = self._create_second_thing()
        self.thing.name= second_thing.name
        self._assert_thing_is_invalid()

    #description  tests
    def test_description_may_be_blank(self):
        self.thing.description= ''
        self._assert_thing_is_valid()

    def test_description_may_already_exist(self):
        second_thing = self._create_second_thing()
        self.thing.description= second_thing.description
        self._assert_thing_is_valid()

    def test_description_may_contain_120_characters(self):
        self.thing.description= 'x' * 120
        self._assert_thing_is_valid()

    def test_description_may_not_contain_over_120_characters(self):
        self.thing.description= 'x' * 121
        self._assert_thing_is_invalid()

    #quantity tests
    def test_description_may_already_exist(self):
        second_thing = self._create_second_thing()
        self.thing.quantity= second_thing.quantity
        self._assert_thing_is_valid()

    def test_quantity_may_be_0(self):
        self.thing.quantity= 0
        self._assert_thing_is_valid()

    def test_quantity_may_not_be_less_than_0(self):
        self.thing.quantity= -1
        self._assert_thing_is_invalid()

    def test_quantity_may_be_100(self):
        self.thing.quantity= 100
        self._assert_thing_is_valid()

    def test_quantity_may_not_be_more_than_100(self):
        self.thing.quantity= 101
        self._assert_thing_is_invalid()

    #assert (in)valid
    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail('Test thing should be valid')

    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()

    def _create_second_thing(self):
        thing = Thing.objects.create_thing(
            name = 'Thing-2',
            description = 'This is the description for thing #2',
            quantity = 57,
        )
        return thing