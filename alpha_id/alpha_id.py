import sys


class AlphaID:
    base_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    global_key = ''

    @staticmethod
    def config(key: str) -> None:
        if not isinstance(key, str):
            raise ValueError('Invalid input. The key must be a string.')
        AlphaID.global_key = key

    @staticmethod
    def convert_number(number: int, key: str = '') -> str:
        if not isinstance(number, (int, int)):
            raise ValueError('Invalid input. The number must be numeric.')

        if key == '':
            key = AlphaID.global_key

        if isinstance(number, int):
            encrypted_number = number ^ AlphaID.crc32(key)
        else:
            encrypted_number = number ^ AlphaID.crc32(key)

        base_length = len(AlphaID.base_chars)
        converted_string = ''
        lookup = list(AlphaID.base_chars)

        while encrypted_number > 0:
            converted_string = lookup[encrypted_number % base_length] + converted_string
            encrypted_number = encrypted_number // base_length

        return converted_string

    @staticmethod
    def recover_number(converted_string: str, key: str = '') -> int:
        if not isinstance(converted_string, str):
            raise ValueError('Invalid input. The encoded string must be a string.')

        if key == '':
            key = AlphaID.global_key

        base_length = len(AlphaID.base_chars)
        recovered_number = 0

        for char in converted_string:
            char_value = AlphaID.base_chars.index(char)
            recovered_number = recovered_number * base_length + char_value

        original_number = recovered_number ^ AlphaID.crc32(key)

        if original_number > sys.maxsize:
            return original_number
        else:
            return int(original_number)

    @staticmethod
    def convert(number_to_be_converted: int, key: str = '') -> str:
        return AlphaID.convert_number(number_to_be_converted, key)

    @staticmethod
    def recover(string_to_be_recovered: str, key: str = '') -> int:
        return AlphaID.recover_number(string_to_be_recovered, key)

    @staticmethod
    def crc32(data: str) -> int:
        crc_table = [0] * 256
        crc = 0xFFFFFFFF

        # Generate CRC32 lookup table
        for i in range(256):
            c = i
            for _ in range(8):
                if c & 1:
                    c = 0xEDB88320 ^ (c >> 1)
                else:
                    c = c >> 1
            crc_table[i] = c

        # Calculate CRC32 checksum
        for byte in data.encode():
            byte = byte & 0xFF
            crc = (crc >> 8) ^ crc_table[(crc ^ byte) & 0xFF]

        crc = crc ^ 0xFFFFFFFF
        return crc & 0xFFFFFFFF
