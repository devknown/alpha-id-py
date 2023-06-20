from alpha_id.alpha_id import AlphaID

alpha_id = AlphaID()

encoded_string = alpha_id.convert(258456357951)
print(encoded_string)
# Output: '4y7exoH'

original_number = alpha_id.recover('4y7exoH')
print(original_number)
# Output: 258456357951