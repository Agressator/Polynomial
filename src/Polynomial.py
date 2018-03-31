
def get_coeffs_and_degrees_from_dict(received_dict):
    degrees_list = []
    coeffs_list = []

    # TODO for python 2.7
    for degree, coef in received_dict.items():
        degrees_list.append(degree)
        coeffs_list.append(coef)
    return degrees_list, coeffs_list

class Polynomial:
    def __init__(self, degree_list, coefs_list):
        if (not isinstance(degree_list, list)) or (not isinstance(coefs_list, list)):
            raise TypeError('Degrees / coefficients must be list')

        if (not len(degree_list)) or (not len(coefs_list)):
            raise TypeError('Degrees / coefficients must be not empty')

        if len(degree_list) != len(coefs_list):
            raise IndexError('The range of degrees and coeefs must be same')

        self.poly_dict = dict()
        for i in range(len(degree_list)):
            if coefs_list[i] != 0:
                if degree_list[i] in self.poly_dict:
                    self.poly_dict[degree_list[i]] += coefs_list[i]
                else:
                    self.poly_dict[degree_list[i]] = coefs_list[i]

        if not len(self.poly_dict):
            self.poly_dict = {0: 0}

    def __str__(self):
        poly_string = '0'
        if self.poly_dict:
            poly_string = ' + '.join(f'{coef}*x^{degree}' for degree, coef in self.poly_dict.items())
        return poly_string

    def __add__(self, other):
        if isinstance(other, Polynomial):
            add_poly_dict = {degree: self.poly_dict.get(degree, 0) + other.poly_dict.get(degree, 0)
                    for degree in set(self.poly_dict) | set(other.poly_dict)}
        elif isinstance(other, (float, int)):
            add_poly_dict = self.poly_dict.copy()
            if 0 in add_poly_dict:
                add_poly_dict[0] += other
            else:
                add_poly_dict[0] = other
        else:
            raise TypeError('Operation type error')
        add_degrees, add_coeffs = get_coeffs_and_degrees_from_dict(add_poly_dict)
        return Polynomial(add_degrees, add_coeffs)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            diff_poly_dict = {degree: self.poly_dict.get(degree, 0) - other.poly_dict.get(degree, 0)
                    for degree in set(self.poly_dict) | set(other.poly_dict)}
        elif isinstance(other, (float, int)):
            diff_poly_dict = self.poly_dict.copy()
            if 0 in diff_poly_dict:
                diff_poly_dict[0] -= other
            else:
                diff_poly_dict[0] = -other
        else:
            raise TypeError('Operation type error')
        diff_degrees, diff_coeffs = get_coeffs_and_degrees_from_dict(diff_poly_dict)
        return Polynomial(diff_degrees, diff_coeffs)

    def __mul__(self, other):
        mul_degrees = []
        mul_coeffs = []

        if isinstance(other, Polynomial):
            for self_degree, self_coef in self.poly_dict.items():
                for other_degree, other_coef in other.poly_dict.items():
                    mul_coeffs.append(self_coef * other_coef)
                    mul_degrees.append(self_degree + other_degree)
        elif isinstance(other, (float, int)):
            for self_degree, self_coef in self.poly_dict.items():
                mul_coeffs.append(self_coef * other)
                mul_degrees.append(self_degree)
        else:
            raise TypeError('Operation type error')

        return Polynomial(mul_degrees, mul_coeffs)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if self.poly_dict == other.poly_dict:
                return True
        elif isinstance(other, (float, int)):
            if (len(self.poly_dict) == 1) and (self.poly_dict[0] == other):
                return True
        return False

    def __ne__(self, other):
        if isinstance(other, Polynomial):
            if self.poly_dict == other.poly_dict:
                return False
        elif isinstance(other, (float, int)):
            if (len(self.poly_dict) == 1) and (self.poly_dict[0] == other):
                return False
        return True