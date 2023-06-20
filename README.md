# alpha-id-py

`alpha-id-py` is a Python library that allows you to generate short alphanumeric strings from integers. It can be useful for creating compact, unique, and obfuscated identifiers.

## AlphaID Library Versions

- [PHP Version](https://github.com/devknown/alpha-id)
- [JavaScript Version](https://github.com/devknown/alpha-id-js)
- [Python Version](https://github.com/devknown/alpha-id-py)

## Installation

You can install `alpha-id-py` using pip:

```bash
pip install alpha-id-py
```

## Getting Started

Simple usage looks like this:

```python
from alpha_id.alpha_id import AlphaID

alpha_id = AlphaID()

encoded_string = alpha_id.convert(258456357951)
print(encoded_string)
# Output: '4y7exoH'

original_number = alpha_id.recover('4y7exoH')
print(original_number)
# Output: 258456357951
```

## Configuring a Global Key

You can set a global key that will be used for encoding and decoding if no specific key is provided. This can be done using the `config` method:

```python
from alpha_id.alpha_id import AlphaID

alpha_id = AlphaID()
alpha_id.config('my_key')

encoded_string = alpha_id.convert(258456357951)
print(encoded_string)
# Output: '4ymMZq9'

original_number = alpha_id.recover('4ymMZq9')
print(original_number)
# Output: 258456357951
```

## License

`alpha-id-py` is open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).
