import random

class SolovayStrassen():
    def isPrime(self, num, k=10):
        if num == 2 or num == 3:
            return True
        if num < 2:
            return False
        if not num & 1:
            return False

        for i in range(k):
            a = random.randrange(2, num - 1)
            x = self.legendre(a, num)
            y = pow(a, (num - 1) // 2, num)
            if (x == 0) or (y != x % num):
                return False

        return True

    def legendre(self, a, num):
        if (a == 0) or (a == 1):
            return a
        if a % 2 == 0:
            r = self.legendre(a // 2, num)
            if num * num - 1 & 8 != 0:
                r *= -1
        else:
            r = self.legendre(num % a, a)
            if (a - 1) * (num - 1) & 4 != 0:
                r *= -1
        return r