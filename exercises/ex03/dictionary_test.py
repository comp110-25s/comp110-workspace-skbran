"""Dictionary tests"""

__author__ = "730547669"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

# tests for invert

def test_invert_use1()-> None:
    """Checks if inverts single characters"""
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_use2()-> None:
    """Checks if inverts longer strings"""
    assert invert({'tommy': 'caldwell', 'janja' : 'garnbret', 'alex': 'honnold'}) == {'caldwell': 'tommy', 'garnbret': 'janja', 'honnold': 'alex'}

def test_invert_edge()-> None:
    """Checks if empty dict returns empty dict"""
    assert invert({}) == {}

#tests for count

def test_count_use1()-> None:
    """Counts climbing holds correctly"""
    assert count(["jug","crimp","sloper","crimp"]) == {"jug":1,"crimp":2,"sloper":1}

def test_count_use2()-> None:
    """Counts numbers correctly"""
assert count(["0","1","2","1","0"]) == {"0":2,"1":2,"2":1}

def test_count_edge()-> None:
    """Checks if empty list returns empty dict"""
    assert count([]) == {}

#tests for favorite_color

def test_fav_use1() -> None:
    """Checks to see if green wins"""
    assert favorite_color({"Sofi": "green", "Noah": "purple", "Walker": "green"}) == "green"

def test_fav_use2() -> None:
    """Checks for a tie, blue should win"""
    assert favorite_color({"Brooke": "blue", "Tommy": "green", "Adam": "blue", "Janja": "green"}) == "blue"

def test_fav_edge() -> None:
    """Checks if empty string elicits no response"""
    assert favorite_color({}) == ""

#tests for bin_len

def test_bin_use1() -> None:
    """checks if correctly measures and sorts climbing strings"""
    assert bin_len(["jug", "bolt", "clip", "nut"]) == {3: {"jug", "nut"}, 4: {"bolt", "clip"}}

def test_bin_use2() -> None:
    """checks if measures characters as length 1"""
    assert bin_len(["g", "u", "m", "b", "y"]) == {1: {"g", "u", "m", "b", "y"}}

def test_bin_edge() -> None:
    """First edge case"""
    assert bin_len([]) == {}