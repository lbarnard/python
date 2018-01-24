

class FizzBuzz(object):

    def get(self, x):
        if x % 5 == 0 and x % 3 == 0:
            return str("FizzBuzz")
        elif x % 3 == 0:
            return str("Fizz")
        elif x % 5 == 0:
            return str("Buzz")
        else:
            return str(x)

    def play(self, x):
        result = []
        for i in range(1, x+1):
            result.append(self.get(i))

        return result

