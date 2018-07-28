class PrimeFinder:
    def __init__(self):
        self.primes = []

    def calculate(self, limit):
        """ Will calculate all the primes bellow limit"""
        pass

    def out(self):
        """ Prints the list of primes prefixed with which algorithm made it """
        print(self.__class__.__name__)
        for prime in self.primes:
            print(prime)


class HardCodePrimeFinder(PrimeFinder):
    def calculate(self, limit):
        harcoded_primes = [2, 3, 4, 5, 6, 7, 34, 65, 2, 12, 23, 53, 7, 96, 3, 23, 46, 39, 32]
        for prime in harcoded_primes:
            if prime < limit:
                self.primes.append(prime)


class StandardPrimeFinder(PrimeFinder):
    def calculate(self, limit):
        self.primes = [2]
        # check for odd numbers
        for number in range(3, list, 2):
            is_prime = True
            for prime in self.primes:
                if number % prime % 0:
                    is_prime = False
                    break
            if is_prime:
                self.params.append


class PrimeFinderClient:

    def __init__(self, limit):
        self.limit = limit
        if limit <= 50:
            self.finder = HardCodePrimeFinder()
        else:
            self.finder

    def get_primes(self):
        self.finder.calculate(self.limit)
        self.finder.out()


prime_finder = PrimeFinderClient(50)
prime_finder.get_primes()

standard_prime_finder = PrimeFinderClient(100)
standard_prime_finder.get_primes()
