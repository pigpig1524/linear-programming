def det(a1, b1, a2, b2):
    """
    This function is used to calculate the det of 2x2 matrix
    Args:
        a1, a2, b1, b2: matrix elements by row
    Return
        det: int
    """
    return a1 * b2 - a2 * b1

def calc_det_equation(func1, target1, func2, target2):
    """
    This function is used to calculate the det of 2 equation
    Args:
        func1, func2 (Function)
        target1, target2: int
    Return
        tupe[int] = (d, dx, dy)
    """
    return (
        det(func1.a, func1.b, func2.a, func2.b), # d
        det(target1, func1.b, target2, func2.b), # dx
        det(func1.a, target1, func2.a, target2)  # dy
    )