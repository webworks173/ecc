# Main program for Elliptic Curve Cryptography (ECC)


class Point(object):
    # This class represents a point on the Elliptic Curve
    def __init__(self, curve, x, y):
        self.curve = curve  # the curve containing this point
        self.x = x
        self.y = y
        if not curve.testPoint(x, y):
            raise Exception("The point %s is not on the given curve %s" % (self, curve))

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)

    def __add__(self, Q):
        if isinstance(Q, Ideal):
            return self

        x_1, y_1, x_2, y_2 = self.x, self.y, Q.x, Q.y

        if (x_1, y_1) == (x_2, y_2):
            # use the tangent method
            ...
        else:
            if x_1 == x_2:
                return Ideal(self.curve)  # vertical line

            # Using Vieta's formula for the sum of the roots
            m = (y_2 - y_1) / (x_2 - x_1)
            x_3 = m * m - x_2 - x_1
            y_3 = m * (x_3 - x_1) + y_1

            return Point(self.curve, x_3, -y_3)


class Ideal(Point):
    # This class represents ideal point
    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Ideal"

    def __neg__(self):
        return self

    def __add__(self, Q):
        return Q


class EllipticCurve(object):
    # This class represents a Elliptic Curve
    def __init__(self,a,b):
        self.a = a
        self.b = b

        # discriminant a function of the coefficients of a polynomial equation whose value gives information
        # about the roots of the polynomial
        # We check that discriminant is nonzero
        # -16(4a^3 + 27b^2) != 0
        self.discriminant = -16 * (4 * a*a*a + 27 * b * b)
        if not self.isSmooth():
            raise Exception("The curve is not smooth! " %self)

    def isSmooth(self):
        # Method which checks for discriminant
        print("Checking curve is smooth or not..")
        return self.discriminant !=0

    def testPoint(self,x,y):
        # Method to check if a Point is on the curve
        print("Checking if point lies on the curve..")
        print('y^2  = {}'.format(y*y))
        print('x^3 + a*x + b = {}'.format((x*x*x + self.a * x + self.b)))
        return y*y == x*x*x + self.a * x + self.b

    def __str__(self):
        return 'y^2 = x^3 + {}Gx + {}G'.format(self.a, self.b)

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)


c = EllipticCurve(a=4, b=4)
# Point(c, 1, 2)

# Un comment Below line to see error
# Point(c, 1, 1)

