import Fizzbuzz
import unittest


class FizzBuzzTest(unittest.TestCase):

    def test_give_3_should_fizz(self):
        data = 3
        expected = 'Fizz'

        # result = fizzbuzz.fizzbuzz(data)

        # self.assertEqual(expected, result)
        result = Fizzbuzz.Fizzz().fizz(data)

        self.assertEqual(expected, result)

    def test_give_12_should_fizz(self):
        data = 12 
        expected = 'Fizz'
        result = Fizzbuzz.Fizzz().fizz(data)
        self.assertEqual(expected, result)

    def test_give_303_should_fizz(self):
        data = 303
        expected = 'Fizz'

        result = Fizzbuzz.Fizzz().fizz(data)

        self.assertEqual(expected, result)


    def test_give_5_should_buzz(self):
        data = 5
        expected = 'Buzz'

        result = Fizzbuzz.Fizzz().buzz(data)
        self.assertEqual(expected, result)


    def test_give_305_should_buzz(self):
        data = 305
        expected = 'Buzz'

        result = Fizzbuzz.Fizzz().buzz(data)
        self.assertEqual(expected, result)


    def test_give_100_should_buzz(self):
        data = 1000
        expected = 'Buzz'

        result = Fizzbuzz.Fizzz().buzz(data)
        self.assertEqual(expected, result)


    def test_give_15_should_fizzbuzz(self):
        data = 15
        expected = 'FizzBuzz'

        result = Fizzbuzz.Fizzz().fizzbuzz(data)
        self.assertEqual(expected, result)



    def test_give_300_should_fizzbuzz(self):
        data = 300
        expected = 'FizzBuzz'

        result = Fizzbuzz.Fizzz().fizzbuzz(data)
        self.assertEqual(expected, result)

    def test_give_1500_should_fizzbuzz(self):
        data = 1500
        expected = 'FizzBuzz'

        result = Fizzbuzz.Fizzz().fizzbuzz(data)

        self.assertEqual(expected, result)