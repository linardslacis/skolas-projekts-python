def elastiba(v0, v1, q0, q1):
    el = ((q1 - q0) / q0) / ((v1 - v0) / v0)
    if abs(el) == 1:
        return print("Elastiba = |1|, pieprasijums ir vienadots")
    elif abs(el) < 1:
        return print("Elastiba =", round(abs(el), 3), ", pieprasijums ir neelastigs")
    else:
        return print("Elastiba =", round(abs(el), 3), ", pieprasijums ir elastigs")


elastiba(2, 4, 5, 25)
