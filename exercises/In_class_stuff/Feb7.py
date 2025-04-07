"""Introducing user input and named constants!"""

SECRET: str = "punk"

def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    """check to see if guessed word is equivalent to the secret word"""
    #if word and secret are different lengths, they clearly aren't the same word.
    #print "Words are different lengths" and return False
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False
    #if words are the same length, move on
    if idx < len(word): #idx is index, ie 3 for a 4 letter word
        if word[idx] != secret[idx]:
            print(f"{word[idx]} isn't the secret word's next letter")
            return False
        else: 
            print(f"{word[idx]} is at index {idx} for both words! Checking next letters...")
            return guess_secret(word = word, secret = secret, idx = idx + 1)
            #this is our recursive case
print("They are the same word!")
return True    