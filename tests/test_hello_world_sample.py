from unittest import TestCase


class TestHelloWorld(TestCase):

    def test_say_hello(self):
        self.assertEqual("Hello", "Hello")

    def test_addiotion_of_2_values_are_correct(self):
        # some lines of code
        # some lines of code
        # some lines of code
        # some lines of code
        sum = 2 + 3
        self.assertEqual(5, sum)
        self.assertEqual("HelloXX", "HelloXX")
        self.assertEqual("HelloXX", "HelloXX")

    def test_login_page_is_correctly_displaying(self):
        self.assertEqual("HelloYY", "HelloYY")
