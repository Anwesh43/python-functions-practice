import sys
import random

# basic functions.
def echo():
    print("hello world")

def sum(a, b):
    return a + b

def printSumNormal():
    print('sum is {0}'.format(sum(30, 40)))

def raiseTo(x):
    def inner(n):
        return x ** n
    return inner

def printCloure():
    print("raising 2 to 3 and 4 times respectively")
    print(raiseTo(2)(3))
    print(raiseTo(2)(4))

def sumArgs(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def printSumArgs():
    print("sum of 1,2,3,8 is {0}".format(sumArgs(1,2,3, 8)))

x = 20

def modifyGlobal():
    global x
    x = 30

def printModfyGlobal():
    def printX():
        print("value of x is {0}".format(x))
    printX()
    modifyGlobal()
    printX()

def useLambdas():
    add = lambda a, b: a + b
    sub = lambda a, b: a - b
    print("addition of 10 and 20 is {0}".format(add(10, 20)))
    print("subtraction of 20 and 10 is {0}".format(sub(20, 10)))

def iterDemo():
    nums = [1, 2, 3, 4, 5] #iterable
    iter_nums = iter(nums) #iterator
    print(next(iter_nums))
    print(next(iter_nums))
    print(next(iter_nums))
    print(list(iter_nums))

def generateAboveFifty():
    num = int(random.random() * 100)
    if num <= 50:
        raise ValueError("num less than 50")
    else:
        return num

def processIfGreaterThanFifty():
    try:
        print("number is {}".format(generateAboveFifty()))
    except ValueError:
        print("number is not greater than 50")

function_dictionary = {"basic": echo, "psn" : printSumNormal, "pc" : printCloure, "psa" : printSumArgs,
"pmg" : printModfyGlobal, "ul" : useLambdas, "idemo" : iterDemo, "re" : processIfGreaterThanFifty}

if __name__ == "__main__":

    args = sys.argv
    if (len(args) == 2):
        method_type = args[-1]
        if (method_type in function_dictionary.keys()):
            function_dictionary[method_type]()
