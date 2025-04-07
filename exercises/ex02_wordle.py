"""A Wordle-Inspired Game"""

__author__: str = "730547669"

def main(secret: str) -> None:
    """The entrypoint of the program"""
    turn_num = 1
    while (turn_num!= 7):
        print(f"=== Turn {turn_num}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn_num}/6 turns")
            return
        turn_num +=1
    print("X/6 - Sorry, try again tomorrow!")

#this function helps us build the emojis based on if it's in the word or not
def contains_char(word: str, char: str) -> bool:
    """Checking if characters match between guesses"""
    assert len(char) == 1, f"len ('{char}') is not 1"
    index = 0
    while index < len(word):
        if word[index] == char:
            return True
        else:
            index += 1
    return False

#checking for letter positioning
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, answer: str) -> str:
    """testing for green, yellow, or white codification"""
    assert len(guess) == len(answer), "Guess must be same length as secret"
    x = 0
    prnt = ""
    while x != len(guess):
        if contains_char(answer, guess[x]) == True:
            if guess[x] == answer[x]:
                prnt += GREEN_BOX
            elif guess[x] != answer[x]:
                prnt += YELLOW_BOX
        else:
            prnt += WHITE_BOX
        x+=1
    return prnt

def input_guess(char_num: int) -> str:
    """gives an expected length of a guess as a parameter"""
    print(f"Enter a {char_num} character word.")
    user_input = str(input())
    while len(user_input) != char_num:
        print(f"That wasn't {char_num} chars! Try again:")
        user_input = input()
    return user_input

if __name__ == "__main__":
    main(secret="codes")