# ocean_animals = ("electric_eel", "jelly_fish", "shrimp", "turtles", "blue_whale")
# def main():
#  for each_animal in ocean_animals:
#   print(f"{each_animal} is an ocean animal")
# if __name__ == "__main__":
#  main()

tupleitems=()
totalitem=int(input("Enter the total number of list"))
for i in range(totalitem):
    userinput=int(input("Enter a number:"))
    tupleitems += (userinput,)
print(f"item added to tuples are{tupleitems}")

list_items=[]
totalitems=int(input("enter the total number of items:"))
for i in range(totalitems):
    item = input("Enter an item to add: ")
    list_items.append(item)
items_of_tuple = tuple(list_items)
print(f"tuples items are{items_of_tuple}")
