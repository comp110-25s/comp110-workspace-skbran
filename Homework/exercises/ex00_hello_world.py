"""My first exercise in COMP110!"""

__author__ = "730547669"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


# def is define, greet is a function name (an identifier)
# first line means: I am defining a function named greet that takes a str parameter named name and returns a str value
if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
