import sys

# basic functions.
def echo():
    print("hello world")

def sum(a, b):
    return a + b

def printSumNormal():
    print('sum is {0}'.format(sum(30, 40)))

function_dictionary = {"basic":echo, "psn" : printSumNormal}
if __name__ == "__main__":

    args = sys.argv
    if (len(args) == 2):
        method_type = args[-1]
        if (method_type in function_dictionary.keys()):
            function_dictionary[method_type]()
