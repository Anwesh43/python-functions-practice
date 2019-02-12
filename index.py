import sys

# basic functions.
def echo():
    print("hello world")

function_dictionary = {"basic":echo}
if __name__ == "__main__":

    args = sys.argv
    if (len(args) == 2):
        method_type = args[-1]
        if (method_type in function_dictionary.keys()):
            function_dictionary[method_type]()
