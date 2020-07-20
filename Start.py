import cf_str

# Input
a = int(input("Enter the first coefficient >>> "))
b = int(input("Enter the second coefficient >>> "))
c = int(input("Enter the third coefficient >>> "))

a_str = cf_str.get_cf_str(a)
b_str = cf_str.get_cf_str(b)
c_str = str(c)

# The actual expression
cf_str.exp_print(a_str, b_str, c_str)

# Get the list that includes the roots
#roots = solveSquare(a, b, c)
