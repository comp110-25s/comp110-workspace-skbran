"""Dictionary!"""

__author__ = "730547669"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    invert_dict: dict[str, str] = {}
    # add original value in my_dict as the key
    for key in my_dict:
        # loop to check for duplicate keys
        if my_dict[key] in invert_dict:
            raise KeyError("Duplicate keys. Try again.")
        invert_dict[my_dict[key]] = key
    return invert_dict


def count(my_list: list[str]) -> dict[str, int]:
    """Counts each value in the input list."""
    # string is the keys, which are from the list
    # int is the values, which is the count of how many times each string appeared
    new_dict: dict[str, int] = {}
    for keys in my_list:
        if keys in new_dict:
            new_dict[keys] += 1
        else:
            # add new key and new value to the new_dict
            new_dict[keys] = 1
    return new_dict


def favorite_color(favs: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    favs_list: list[str] = []
    for name in favs:
        favs_list.append(favs[name])
    favs_dict = count(favs_list)   # returns dict of colors and frequency of each color
    max_freq: int = 0
    max_color: str = ""
    for color in favs_dict:
        if favs_dict[color] > max_freq:
            max_freq = favs_dict[color]
            max_color = color
    return max_color


def bin_len(my_list: list[str]) -> dict[int, set]:
    """Returns lengths of strings in a list."""
    bin_dict: dict[int, set] = {}
    for each_string in my_list:
        if len(each_string) in bin_dict:
            bin_dict[len(each_string)].add(each_string)
        else:
            bin_dict[len(each_string)] = {each_string}
    return bin_dict
