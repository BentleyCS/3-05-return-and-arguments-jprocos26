def convertTemperature(temp):
    unit = temp[-1]
    
    number = float(temp[:-1])
    
    if unit == "F":
        celsius = (number - 32) * 5 / 9
        return str(int(celsius)) + "C"
    elif unit == "C":
        fahrenheit = (number * 9 / 5) + 32
        return str(int(fahrenheit)) + "F"

def larger(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num

def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n / 2
    else:
        return n * 3 + 1

