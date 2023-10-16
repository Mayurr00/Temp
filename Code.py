a = 5
b = 6
c = 7

semi_perimeter = (a+b+c)/2

area = (semi_perimeter*(semi_perimeter-a)*(semi_perimeter-b)*(semi_perimeter-c))**0.5

print(f'The area of the triangle is with sides as ({a}, {b}, {c}) is {area}')