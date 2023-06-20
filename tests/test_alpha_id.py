import unittest
from alpha_id.alpha_id import AlphaID

class AlphaIDTests(unittest.TestCase):
    def setUp(self):
        AlphaID.config('globalkey')

    def test_encode_and_decode_with_global_key(self):
        number = 1234567890

        encoded = AlphaID.convert(number)
        decoded = AlphaID.recover(encoded)

        self.assertEqual(decoded, number)

    def test_encode_and_decode_with_specific_key(self):
        number = 987654321
        key = 'specifickey'

        encoded = AlphaID.convert(number, key)
        decoded = AlphaID.recover(encoded, key)

        self.assertEqual(decoded, number)

    def test_encode_and_decode_with_empty_key(self):
        number = 54321

        encoded = AlphaID.convert(number, '')
        decoded = AlphaID.recover(encoded, '')

        self.assertEqual(decoded, number)

    def test_encode_number_to_encoded_string(self):
        test_data = [
            (123456, '3ygxRZ'),
            (987654, '3ycMuJ'),
            (54321, '3ygih0'),
            (89815, '3ygH9C'),
        ]

        for number, expected_encoded_string in test_data:
            encoded = AlphaID.convert(number)
            self.assertEqual(encoded, expected_encoded_string)

    def test_decode_encoded_string_to_number(self):
        test_data = [
            ('3ygxRZ', 123456),
            ('3ycMuJ', 987654),
            ('3ygih0', 54321),
            ('3ygH9C', 89815),
        ]

        for encoded_string, expected_number in test_data:
            decoded = AlphaID.recover(encoded_string)
            self.assertEqual(decoded, expected_number)


if __name__ == '__main__':
    unittest.main()
