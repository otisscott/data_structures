import math

allowed_num = False
dec_num = 0
while not allowed_num:
    dec_num = int(input('Enter a number greater than or equal to 0: '))
    if dec_num >= 0:
        allowed_num = True
original_num = dec_num
bin_str = ''
while dec_num > 0:
    bit = dec_num % 2
    bin_str = str(bit) + bin_str
    print(str(dec_num), ' %  2 = ', str(bit), ' --- ', bin_str)
    new_dec = math.floor(dec_num/2)
    print(str(dec_num), ' / 2  = ', str(new_dec))
    dec_num = new_dec

print(str(original_num), ' in binary is ', bin_str)
