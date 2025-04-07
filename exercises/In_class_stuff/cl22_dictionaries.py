"""Examples of dictionary syntac with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"]+=110
print(ice_cream["vanilla"])
print(ice_cream["pecan"])