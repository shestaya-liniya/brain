def convert_base(value, final_base):
    while value > 0:    
        digit = value % final_base
        value //= final_base

        print(digit, end="")


convert_base(1234, 10)
