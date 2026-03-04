import math
def area_of_triangle (a, b, c) :
    if a + b <= c or a + c <= b or b + c <= a :
        return 0
    s = (a + b + c) / 2
    area = math.sqrt (s * (s - a) * (s - b) * (s - c))
    return area

a, b, c = map (float, input ("3ta  bahur value enter koren").split ())
ar = area_of_triangle (a, b, c)
print('triangle sovob na ' if ar == 0 else f'area_of_triangle: {ar:.2f}')

import math

def area_of_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 0
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a, b, c = map(float, input("3ta bahur value enter koren: ").split())
ar = area_of_triangle(a, b, c)

print("triangle sovob na" if ar == 0 else f"area_of_triangle: {ar:.2f}")
