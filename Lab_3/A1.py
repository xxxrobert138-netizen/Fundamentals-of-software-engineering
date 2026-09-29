def determine_quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return None

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

q1 = determine_quarter(x1, y1)
q2 = determine_quarter(x2, y2)

v = ["I", "II", "III", "IV"]
print(f"YES, {v[q1 - 1]}" if q1 == q2 else f"NO")