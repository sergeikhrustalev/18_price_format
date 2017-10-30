import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):

    def test_price_empty_string_value(self):
        self.assertIsNone(format_price(''))

    def test_price_incorrect_value(self):
        self.assertIsNone(format_price('erjeghrd'))

    def test_price_negative_value(self):
        self.assertIsNone(format_price('-45.0002'))

    def test_price_round_to_number(self):
        self.assertEqual(
            format_price('23.985768'), '24'
        )

    def test_price_format_number(self):
        self.assertEqual(
            format_price('3245.000000'), '3 245'
        )

    def test_price_format_big_number(self):
        self.assertEqual(
            format_price('12345678.00002222'), '12 345 678'
        )

    def test_price_format_very_big_number(self):
        self.assertEqual(
            format_price('45123456754.99992222'), '45 123 456 755'
        )


if __name__ == '__main__':
    unittest.main()
