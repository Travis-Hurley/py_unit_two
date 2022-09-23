value = input('How much money?')
decimized_value = float(value)
hundred_division=decimized_value//100
hundred_remainder= round(decimized_value%100,2)
if hundred_remainder > 50:
    fifty_division=hundred_remainder//50
    fifty_remainder=round(hundred_remainder%50,2)
if fifty_remainder > 10:
    ten_dividion=fifty_remainder//10
    ten_remainder=round(fifty_remainder%10,2)
print(ten_dividion,ten_remainder)