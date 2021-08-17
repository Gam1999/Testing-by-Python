class Fizzz:
    def fizzbuzz(self, num):
        if num%3 == num%5 == 0:
            return 'FizzBuzz'

    def fizz(self, num):
        if num%3 == 0:
            return 'Fizz'

    def buzz(self, num):
        if num%5 == 0:
            return 'Buzz'
