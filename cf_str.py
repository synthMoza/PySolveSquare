def get_cf_str(input_number : int) -> str:
    """ Returns the string coefficient of the given number for printing the equation (for cases like -1, 1)"""
    if input_number == -1:
        return "-"
    elif input_number == 1:
        return ""
    else:
        return str(input_number )

def exp_print(a_str : str, b_str : str, c_str : str) -> None:
    """ Print the square equation with the given coefficients nicely """
    result_str = ""

    if a_str == "0":
        if b_str == "0":
            if c_str =="0":
                # All coefficients equal zero
                result_str = '0 = 0'
            else:
                # Only c != 0
                result_str = c_str 
        else:
            # Only a == 0
            if c_str[0] == '-':
                result_str = b_str + "x " + c_str
            else:
                result_str = b_str + "x + " + c_str
    else:
        # a != 0
        result_str = a_str + "x^2"
        if  b_str[0] != '-' and b_str != "0":
            result_str += "+"
        if b_str != "0":
            result_str += (b_str + "x")
        if c_str[0] != '-' and c_str != "0":
            result_str += "+"
        if c_str != "0":
            result_str += c_str

    # Print the result
    print("The equation is", result_str, "= 0")
