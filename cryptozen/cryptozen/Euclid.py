import time
import cryptozen.RSAkeys


class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def gcd(self):
        q = self.a
        p = self.b
        if p == 0 and q == 0:
            raise Exception("GCD of 0 with 0 is not defined")
        if isinstance(p, float) and p.is_integer() == False:
            raise Exception("This is not yet built into")
        if isinstance(q, float) and q.is_integer() == False:
            raise Exception("This is not yet built into")
        if isinstance(q, float) and q.is_integer() == True:
            q = int(q)
        if isinstance(p, float) and p.is_integer() == True:
            p = int(p)
        while q != 0:
            x = time.time()
            q, p = p % q, q
            if (time.time() - x) * 1000 > 120:
                raise Exception("The gcd has taken too long to respond")
        return p

    def extended_gcd(self):
        if abs(self.gcd()) != 1:
            return None

        v1, v2, v3 = 0, 1, self.b
        u1, u2, u3 = 1, 0, self.a
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (
                (u1 - q * v1),
                (u2 - q * v2),
                (u3 - q * v3),
                v1,
                v2,
                v3,
            )
        return u1 % self.b
