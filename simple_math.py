# This file describes some basic math functions to explain how variables,
# arguments, parameters, and functions work.

# This function takes in two arguments and returns their sum.
# The variables x and y are called parameters of the function add
# because they are in the parentheses.
# The values of those variables, for example 2 and 3 in the function
# call add(2, 3) in main() below, are called arguments.
# This function returns a value that can be stored by assigning the value
# of the expression add(2, 3) to a name, such as z.
def add(x, y):
    return x + y

def main():
    # The variable z stores the return value of the function add.
    z = add(2, 3)
    print(z)

if __name__ == "__main__":
    main()
