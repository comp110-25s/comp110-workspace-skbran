"""Calculate how many tea bags, treats, and money are needed to throw a tea party for an inputted number of guests"""

__author__: str = "730547669"

def main_planner(guests: int) -> None:
    """sets up parameters for other functions and print statements"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return None

def tea_bags(people: int) -> int:
    """return number of necessary tea bags"""
    return 2 * people

def treats(people: int) -> int:
    """return number of necessary treats"""
    return int(tea_bags(people=people) * 1.5)

def cost(tea_count: int, treat_count: int) -> float:
    """return cost of tea party"""
    return tea_count * 0.5 + treat_count * 0.75

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
