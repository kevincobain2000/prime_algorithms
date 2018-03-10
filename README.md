# prime_algorithms

Currently, this package provides a few prime number algorithms.

### Requirements

python >= 2.7 or >= 3.0

### Installation

```
python setup.py install
```

```
from prime_algorithms.algorithms.millerrabin import MillerRabin
from prime_algorithms.algorithms.squareroot import SquareRoot
from prime_algorithms.algorithms.sixk import SixK
from prime_algorithms.algorithms.solovaystrassen import SolovayStrassen


num = 3

//fast methods
MillerRabin().isPrime(num)
SolovayStrassen().isPrime(num)

//slow methods
SquareRoot().isPrime(num)
SixK().isPrime(num)
```

# How to Contribute

- provide a method isPrime to your algorithm.
- ``NameOfYourAlgorithm.isPrime(num)``

### References

- https://math.stackexchange.com/questions/1187491/prime-numbers-6k-1-mod-rule-new-discovery
- https://www.youtube.com/watch?v=lEvXcTYqtKU (00:00 - 00:15 )
- https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
- https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test
- https://coderwall.com/p/utwriw/prime-numbers-with-python
- https://primes.utm.edu/lists/small/