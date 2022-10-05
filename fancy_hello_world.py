# This is a fancier hello world that uses a main function

# This is a function called main. The word "def" is used
# to indicate that we are starting a function definition.
# The parentheses can hold parameters (variables that store
# the values of arguments that you pass to the function).
# This function has no parameters (it takes no arguments)
def main():
    print("hello world")

# The name of the "module" is "__main__" by default. The
# variable __name__ is defined automatically in every python
# program. Doing this will run your main function. We need this bit
# of code in case the main function lives in another file that we
# imported.
if __name__ == "__main__":
    main()
