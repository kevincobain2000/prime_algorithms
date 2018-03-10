class SquareRoot():
    def isPrime(self, num):
        '''check if integer num is a prime'''

        # make sure num is a positive integer
        num = abs(int(num))

        # 0 and 1 are not primes
        if num < 2:
            return False

        # 2 is the only even prime number
        if num == 2:
            return True

        # all other even numbers are not primes
        if not num & 1:
            return False

        # range starts with 3 and only needs to go up
        # the square root of num for all odd numbers

        i = 3
        j = int(self.sqrt(num)) + 1
        k = 2
        while i < j:
            i += 2
            if num % i == 0:
                return False

        return True
    # Methods from Stack overflow flow to handle large bits
    def sqrt(self, num):
        i = num.bit_length() >> 1    # i = floor( (1 + floor(log_2(num))) / 2 )
        m = 1 << i    # m = 2^i
        #
        # Fact: (2^(i + 1))^2 > num, so m has at least as many bits
        # as the floor of the square root of num.
        #
        # Proof: (2^(i+1))^2 = 2^(2i + 2) >= 2^(floor(log_2(num)) + 2)
        # >= 2^(ceil(log_2(num) + 1) >= 2^(log_2(num) + 1) > 2^(log_2(num)) = num. QED.
        #
        while m*m > num:
            m >>= 1
            i -= 1
        for k in range(i-1, -1, -1):
            x = m | (1 << k)
            if x*x <= num:
                m = x
        return m