import sys

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

function_dictionary = {"basic":echo, "psn" : printSumNormal, "pc" : printCloure}
if __name__ == "__main__":

    args = sys.argv
    if (len(args) == 2):
        method_type = args[-1]
        if (method_type in function_dictionary.keys()):
            function_dictionary[method_type]()
