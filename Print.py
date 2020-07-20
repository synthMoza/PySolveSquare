
def print_roots(roots : list) -> None:
    """ Prints the roots from the given list """
    number = len(roots)
    if number == 0:
        print("There are no real roots.")
    elif roots[0] == "inf":
        print("This equation has infinite number of roots")
    elif number == 1:
        print("The only root of this equation: x =", roots[0])
    else:
        print("THere are two roots: x1 =", roots[0], "x2 =", roots[1])
