from django.test import TestCase
from .models import Thing
from django.core.exceptions import ValidationError

class ThingModelTestCase(TestCase):
    def setUp(self):
        self.user = Thing.objects.create_user(
            name = 'Thing-1',
            description = 'This is the description for thing #1',
            quantity = 23,
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

    #name tests
    def test_name_cannot_be_blank(self):
        self.user.name=''
        self._assert_user_is_invalid()

    def test_name_can_be_30_characters_long(self):
        self.user.name= 'x' * 30
        self._assert_user_is_valid()

    def test_name_cannot_be_over_30_characters_long(self):
        self.user.name= 'x' * 31
        self._assert_user_is_invalid()

    def test_name_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.name= second_user.name
        self._assert_user_is_invalid()

    #description  tests
    def test_description_may_be_blank(self):
        self.user.description= ''
        self._assert_user_is_valid()

    def test_description_may_already_exist(self):
        second_user = self._create_second_user()
        self.user.description= second_user.description
        self._assert_user_is_valid()

    def test_description_may_contain_120_characters(self):
        self.user.description= 'x' * 120
        self._assert_user_is_valid()

    def test_description_may_not_contain_over_120_characters(self):
        self.user.description= 'x' * 121
        self._assert_user_is_invalid()

    #quantity tests
    def test_description_may_already_exist(self):
        second_user = self._create_second_user()
        self.user.quantity= second_user.quantity
        self._assert_user_is_valid()

    def test_quantity_may_be_0(self):
        self.user.quantity= 0
        self._assert_user_is_valid()

    def test_quantity_may_not_be_less_than_0(self):
        self.user.quantity= -1
        self._assert_user_is_invalid()

    def test_quantity_may_be_100(self):
        self.user.quantity= 100
        self._assert_user_is_valid()

    def test_quantity_may_not_be_more_than_100(self):
        self.user.quantity= 101
        self._assert_user_is_invalid()

    #assert (in)valid
    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def _create_second_user(self):
        user = Thing.objects.create_user(
            name = 'Thing-2',
            description = 'This is the description for thing #2',
            quantity = 57,
        )
        return user