'''
@author dsindl
'''


class Bruch(object):
    '''
    :param int zaehler: numerator
    :param int nenner: denominator
    :ivar int zaehler: numerator
    :ivar int nenner: denominator
    '''

    def __iter__(self):
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):
        '''
        Ueberprueft auf Fehler (falscher Datentyp, division bei 0)
        :param zaehler:
        :param nenner:
        '''
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('falscher typ:' + type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('falscher typ:' + type(nenner).__name__)
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner

    def __float__(self):
        '''

        :return: float
        '''
        return self.zaehler / self.nenner

    def __int__(self):
        '''

        :return: int
        '''
        return int(self.__float__())

    def __neg__(self):
        '''

        :return: Bruch
        '''
        return Bruch(-self.zaehler, self.nenner)

    def __radd__(self, zaehler):
        '''

        :param zaehler:
        :return: Bruch
        '''
        return self.__add__(zaehler)

    def __add__(self, zaehler):
        '''

        :param zaehler:
        :return: Bruch
        '''
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('falscher typ:' + type(zaehler).__name__ )
        nennerNeu = self.nenner * n2
        zaehlerNeu = z2 * self.nenner + n2 * self.zaehler
        return Bruch(zaehlerNeu, nennerNeu)

    def __complex__(self):
        '''

        :return: complex
        '''
        return complex(self.__float__())

    def __rsub__(self, left):
        '''

        :param left: int oder Bruch
        :return: Bruch
        '''
        if type(left) is int:
            z2 = left
            nennerNeu = self.nenner
            zaehlerNeu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError('falscher typ' + type(left).__name__ )

    def __sub__(self, zaehler):
        '''

        :param zaehler: int oder Bruch
        :return: Bruch
        '''
        return self.__add__(zaehler * -1)

    def __rmul__(self, zaehler):
        '''

        :param zaehler: int oder Bruch
        :return: Bruch
        '''
        return self.__mul__(zaehler)

    def __mul__(self, zaehler):
        '''

        :param zaehler: int oder Bruch
        :return: Bruch
        '''
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('falscher typ:' + type(zaehler).__name__ )
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)

    def __pow__(self, p):
        '''

        :param p: int
        :return: Bruch
        '''
        if type(p) is int:
            return Bruch(self.zaehler ** p, self.nenner ** p)
        else:
            raise TypeError('kein int:' + type(p).__name__ )



    def __rdiv__(self, left):
        '''

        :param left: int oder Bruch
        :return: Bruch
        '''
        if type(left) is int:
            z2 = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('falscher typ:' + type(left).__name__ )


    def __div__(self, zaehler):
        '''

        :param zaehler: int oder Bruch
        :return: Bruch
        '''
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('falscher typ:' + type(zaehler).__name__ )
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))

    def __invert__(self):
        '''

        :return: Bruch
        '''
        return Bruch(self.nenner, self.zaehler)
    def __repr__(self):
        '''

        :return: str
        '''
        shorten = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)


    def __makeBruch(other):
        '''

        :return: Bruch
        '''
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError('weder int noch bruch:' + type(other).__name__ )

    def __eq__(self, other):
        '''

        :param other: other Bruch
        :return: boolean
        '''
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner

    def __ne__(self, other):
        '''

        :param other: other Bruch
        :return: boolean
        '''
        return not self.__eq__(other)

    def __gt__(self, other):
        '''

        :param other: other Bruch
        :return: boolean
        '''
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner

    def __lt__(self, other):
        '''

        :param other: other Bruch
        :return: boolean
        '''
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner

    def __ge__(self, other):
        '''

        :param other: other Bruch
        :return: boolean
        '''
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner

    def __le__(self, other):
        '''

        :param other: other Bruch
        :return: boolean
        '''
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner <= other.zaehler * self.nenner

    def __abs__(self):
        '''

        :return: Bruch
        '''
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __iadd__(self, other):
        '''

        :param other: Bruch
        :return: self
        '''
        other = Bruch.__makeBruch(other)
        self = self + other
        return self

    def __isub__(self, other):
        '''

        :param other: Bruch
        :return: self
        '''
        other = Bruch.__makeBruch(other)
        self = self - other
        return self

    def __imul__(self, other):
        '''

        :param other: other Bruch
        :return: self
        '''
        other = Bruch.__makeBruch(other)
        self = self * other
        return self


    def __idiv__(self, other):
        '''

        :param other: other Bruch
        :return: self
        '''
        other = Bruch.__makeBruch(other)
        self = self / other
        return self

    @classmethod
    def gcd(cls, x, y):
        '''

        :param x:
        :param y:
        :return: hoechster divisor
        '''
        x, y = abs(x), abs(y)
        if x < y: x, y = y, x
        while y != 0:
            x, y = y, x % y
        return x
