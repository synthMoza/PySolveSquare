from cf_str import get_cf_str
from cf_str import exp_print
from Solve import solveSquare
from Print import print_roots

# Input
a = int(input("Enter the first coefficient >>> "))
b = int(input("Enter the second coefficient >>> "))
c = int(input("Enter the third coefficient >>> "))

a_str = get_cf_str(a)
b_str = get_cf_str(b)
c_str = str(c)

# The actual expression
exp_print(a_str, b_str, c_str)

# Get the list that includes the roots and print them
roots = solveSquare(a, b, c)
print_roots(roots)
