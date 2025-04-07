"""Examples of set and dictionary syntax."""


pids: set[int] = {710000000, 712345768}

pids.add(730120710)

ice_cream: dict[str, str] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
} # type: ignore

#update value of vanilla to an additional 110 orders
ice_cream["vanilla"]+=110
#add 3 orders of mint to the dictionary
ice_cream["mint"]=3
#print out number of orders of chocolate
ice_cream["chocolate"]
#update number of orders of vanilla to 10
ice_cream["vanilla"]= 10

#check if mint and chocolate are in ice_cream

"mint" in ice_cream
"chocolate" in ice_cream

#conditional
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")

#remove key value pair associated with a key

ice_cream.pop("strawberry")

#for loops, iterate over keys by default
#print all flavors
for key in ice_cream:
    print(key)

for key in ice_cream:
    print(ice_cream[key])