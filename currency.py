value = input('How much money?')
decimized_value = float(value)
hundred_division=decimized_value//100
hundred_remainder= round(decimized_value%100,2)
if hundred_remainder > 50:
    fifty_division=hundred_remainder//50
    fifty_r = round(hundred_remainder % 50, 2)
if fifty_r > 10:
    ten_dividion = fifty_r//10
    ten_r =round(fifty_r%10,2)
if ten_r>5:
    five_d=ten_r//5
    five_r=round(ten_r%5,2)
if five_r>1:
    one_d=five_r//1
    one_r =round(five_r%1,2)
if one_r>0.25:
    quarter_d=one_r//0.25
    quarter_r=round(one_r%0.25,2)
if quarter_r>0.10:
    dime_d=quarter_r//0.10
    dime_r=round(quarter_r%.10,2)
if dime_r>0.05:
    nickel_division = dime_r%0.05
    nickle_r=dime_r//0.05
if nickle_r>0.01:
    p_d=nickle_r//0.01
    p_r=round(nickle_r%0.01,2)
print(nickle_r,nickel_division)

