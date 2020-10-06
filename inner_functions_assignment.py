def measurements(length, width):

    def area(l_variable, w):
        area_result = l_variable * w
        return area_result

    A1 = area(length, width)

    def perimeter(l_variable, w):
        perimeter_result = 2*(l_variable+w)
        return perimeter_result

    P1 = perimeter(length, width)

    return "Perimeter = "+str(P1)+" Area = "+str(A1)






