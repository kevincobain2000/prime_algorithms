import sys

from prime_algorithms.algorithms.millerrabin import MillerRabin
from prime_algorithms.algorithms.squareroot import SquareRoot
from prime_algorithms.algorithms.sixk import SixK
from prime_algorithms.algorithms.solovaystrassen import SolovayStrassen
import time

if __name__ == "__main__":
    miller_rabin = MillerRabin()
    square_root = SquareRoot()
    six_k = SixK()
    solovay_strassen = SolovayStrassen()

    for num in [3, 4, 5]:
        print(num)
        print("MillerRabin:" + str(miller_rabin.isPrime(num)))
        print("SquareRoot:" + str(square_root.isPrime(num)))
        print("SixK:" + str(six_k.isPrime(num)))
        print("SolovayStrassen:" + str(solovay_strassen.isPrime(num)))


    three_hundred_digit = 203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123
    start_time = time.time()
    print("MillerRabin:" + str(miller_rabin.isPrime(three_hundred_digit)))
    print("--- %s seconds ---" % (time.time() - start_time))