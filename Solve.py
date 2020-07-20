from math import sqrt

def solveSquare(a : int, b : int, c : int) -> list:
    """ Solves a square equation with the given coefficients (ax^2 + bx + c = 0), returns the list of roots"""
    roots = []

    if a == 0:
        return solveLinear(b, c)
    else:
        # The square case
        
        # The discriminant
        disc = b * b - 4 * a * c

        # No roots
        if disc < 0:
            return roots
        # The only one root
        if disc == 0:
            root = -b / (2 * a)
            roots.append(root)
            return roots
        # Two roots
        else:
            disc = sqrt(disc)
            root_1 = (-b + disc) / (2 * a)
            root_2 = (-b - disc) / (2 * a)
            roots.append(root_1)
            roots.append(root_2)
            return roots

def solveLinear(b : int, c : int) -> list:
    """ Sovles a linear equation with the given coefficients (bx + c = 0)"""
    roots = []
    if b == 0:
            if c == 0:
                # Infinite amount of roots
                roots.append("inf")
                return roots
            else:
                # No roots
                return roots
    else:
        # One root
        roots.append(-c / b)
        return roots
