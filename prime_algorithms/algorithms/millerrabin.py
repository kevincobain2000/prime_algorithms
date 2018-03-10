import random

class MillerRabin():
    def isPrime(self, num, k=100):
        if num == 2 or num == 3:
            return True
        if num < 2:
            return False
        if not num & 1:
            return False

        d = (num-1) >> 1
        s = 1
        while not (d & 1):
            d = d >> 1
            s += 1
        for i in range(k):
            a = random.randint(2, num-2)
            x = pow(a, d, num)
            if not (x == 1 or x == num-1):
                for i in range(s-1):
                    x = (x**2) % num
                    if x == 1:
                        return False
                    if x == num-1:
                        break
                if not x == num-1:
                    return False
        return True