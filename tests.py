import unittest

from format_price import format_price


class PriceTestCase(unittest.TestCase):
    def test_none_price(self):
        price = format_price(None)
        self.assertEqual(price, '')

    def test_int_price(self):
        price = format_price(4323)
        self.assertEqual(price, '4 323')

    def test_int_price_with_delimiter(self):
        price = format_price(4672.00)
        self.assertEqual(price, '4 672')

    def test_float_price(self):
        price = format_price(4672.03567)
        self.assertEqual(price, '4 672.04')

    def test_str_price_with_delimiter(self):
        price = format_price('25694,03567')
        self.assertEqual(price, '25 694.04')

    def test_str_price_with_rigth_delimiter(self):
        price = format_price('25694.03567')
        self.assertEqual(price, '25 694.04')

    def test_str_price(self):
        price = format_price('2569')
        self.assertEqual(price, '2 569')

    def test_str_price_in_right_exp_format(self):
        price = format_price('1.2354e+4')
        self.assertEqual(price, '12 354')

    def test_str_price_in_exp_format(self):
        price = format_price('1,2354453E+4')
        self.assertEqual(price, '12 354.45')

    def test_incorrect_value(self):
        price = format_price('1,235б453E+4')
        self.assertEqual(price, 'Incorrect value')


if __name__ == '__main__':
    unittest.main()
