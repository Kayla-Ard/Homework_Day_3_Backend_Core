# Python Lists
# Ordered Collection of items, where each item has a specific place, known as an index

# declaring list variables
# empty list
empty_list = [] #square brackets is always a list

# a list with stuff in it
# each item in a list needs to be separated by a comma
potions = ["Healing", "Invisiblity", "Strength"]

print(potions)

# positions in a list - index
# index 0 is always the first position
# -1 this is always the last position, regardless of list length
#             0            1              2 or -1
potions = ["Healing", "Invisiblity", "Strength"]

# accessing items in a list by index
# list_variable[index_number] - index will always be an integer
# access the first position of my potions list
print(potions[0]) # "Healing"

my_potion = potions[1]

print(my_potion)

# accessing the last item in our list
# with the index number itself or -1
print(potions[2])
print(potions[-1])

# Lists maintain the order we set
colors = ["red", "blue", "green", "yellow"]
print(colors)

# Python's dynamic typing
my_variable = "string"
my_variable = 5
# variables arent locked to a specific type upon declaration

# Python lists are hella flexible
#             0      1     2          3
weird_list = [12, "Duck", 5.46, ["Bob", "Linda"]]
print(weird_list)
print(weird_list[3][1])
print(weird_list[-1])
print(weird_list[-1][-1])


# How do we add and remove things to our list
# .append()
# our_list.append(thing we're appending)
golf_supplies = ["Golf Cart", "Golf Balls", "Golf Clubs"]
golf_supplies.append("Ball Polisher")
print(golf_supplies)
golf_supplies.append("Vizor")
golf_supplies.append("Caddy")
print(golf_supplies)

# removing from a list in python
# ourlist.remove(thing we're removing)
# ourlist.pop() #removes by index and if no argument is provided, it pops the last index
# pop also returns the value that is popped
# del our_list[postion]
# our_list.clear() clears out the list 


golf_supplies.remove("Ball Polisher") # returns None
print(golf_supplies)
# golf_supplies.remove() TypeError because remove takes exactly 1 argument and weve given 0

popped_item = golf_supplies.pop() #no argument so its going to default to -1 -> last index
print(popped_item)
# returns the item that was popped
print(golf_supplies)
# popping an item with an index
print(golf_supplies.pop(1))
print(golf_supplies)

# del which just wipes whatever it is we're delling
# be careful with del because it is quite unforgiving
adventuring_supplies = ["Sword", "Canteen", "Potions", "Cape", "Rope", "Alternator", "Fruit Snacks"]
print(adventuring_supplies)
del adventuring_supplies[1]
print(adventuring_supplies)
# del adventuring_supplies
# print(adventuring_supplies)

adventuring_supplies.clear()
print(adventuring_supplies)

# Lists with duplicate items
flowers = ["rose", "lily", "rose", "daisy", "lily", "rose", "its been 84 years"]
# our_list.count(the thing we're counting)
print(flowers.count("rose"))

lilies = flowers.count("lily")
print(lilies)
flowers.remove("rose") # this removes only the first occurence
print(flowers)

more_flowers = ["rose", "lily","rose", "rose", "daisy", "lily", "rose", "its been 84 years"]
# trying to remove with a for loop
for flower in more_flowers:
    if flower == "rose":
        more_flowers.remove(flower)
print(more_flowers)

while "rose" in more_flowers:
    more_flowers.remove("rose")
print(more_flowers)

# adding to a list by postion
# our_list.insert(postion, thing we're inserting)
hobbies = ["video games", "kayaking", "golfing", "drankin"]
hobbies.insert(2, "hiking")
print(hobbies)
hobbies.insert(3, "reading")
print(hobbies)
hobbies.insert(1, "basketball")
print(hobbies)

# ====================== SORTING LISTS ==========================
# our_list.sort() -> alter our original list and sort it - in place
# sorted(our_list) -> copies our list and sorts the copy - out of place
numbers = [5, 1, 6, 100, 13, 2, 4, 17, 12]
print("numbers before .sort", numbers)
numbers.sort()
print("numbers after .sort", numbers)

# reverse sorting a list
even_more_numbers = [5, 1, 6, 100, 13, 2, 4, 17, 12]
even_more_numbers.sort(reverse=True)
print(even_more_numbers)

more_numbers = [5, 1, 6, 100, 13, 2, 4, 17, 12]
sorted_numbers = sorted(more_numbers) #reverse=True can go in the parentheses as an additional argument
print(more_numbers, "unchanged")
print(sorted_numbers, "copy is sorted")

# len() -> length or how many items are inside our list
names = ["Chris", "Farzin", "Victor", "Winter", "Karen", "andy"]
print(len(names))

names.sort()
print(names)
# our_list.reverse()
# names.reverse()
# print(names)

# Checking if two variables are pointing to the same list object
guest_1 = [1, 2, 3]
guest_2 = guest_1
guest_3 = [1, 2, 3]

print(guest_1 is guest_2)
print(guest_1 is guest_3)
print(guest_1 == guest_3)

# Membership check in a list using in
guest_list = ["Alice", "Bob", "Charlie"]
print("Alice" in guest_list) # True
print("Dana" in guest_list) # False

if "Bob" in guest_list:
    print("awww shooot, who invited Bob?")
else:
    print("Oh thank god, no Bob!")

print("Bob" not in guest_list) # False

guestlist_a = ["Alice", "Bob", "Charlie"]

guestlist_b = ["Alice", "Charlie", "Stephen"]

if guestlist_a[1] in guestlist_b:
    print("We should definitely invite ", guestlist_a[0])
else:
    print("maybe we wont invite them")

# Deeper Dive of len()
hobbies = ["video games", "golfing", "hiking", "basketball", "reading"]
print(len(hobbies)) # number of items in my list
# 0 1 2 3
print(hobbies[len(hobbies) - 1]) #accessing the last item in our list using len(list) - 1
#                4        - 1  =  3
last_index = len(hobbies) - 1 # 3
print(hobbies[last_index]) #hobbies[3] or hobbies[-1]

# setting other postions to variables
# use those variables to index into the list
position = 2
favorite_hobby = hobbies[position]
print(favorite_hobby)

# using the floor operator to grab the middle index of our list
middle_index = len(hobbies) // 2
print(len(hobbies))
print(len(hobbies)/2)
print(middle_index)
print(hobbies[middle_index])




# Concatenation or Combingin lists
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "peas"]

weird_salad = fruits + vegetables # combines fruits list with vegetables list
print(weird_salad)


# list.copy()
salad_clone = weird_salad.copy()
print(salad_clone)

# list.extend()
vegetables.extend(fruits)
print(vegetables)

# " ".join(our_list) -> joins the elements of a list together based on a joiner
story_time = ["once", "upon", "a", "time", "there", "lived", "an", "ogre"]
our_story = " ".join(story_time)
print(our_story.capitalize()) #capitalize() captialzies the first letter of our string


# ============= LIST SLICING =============
# allows us to grab specifc chunks or slices of our list
#           included     not included
#             0 default   last index    1
# our_list[start index:stop index:step index]
#              0            1        2          3         4              5       6          7            8
hobbies = ["video games", "golf", "hiking", "reading", "basketball", "anime", "chess", "opal mining", "soccer"]
print(hobbies[2:]) #slice from index 2 to the rest of my list
# creating a new list variable with a slice
fav_hobbies = hobbies[3:6] # slices starting at reading and stops right before index 6 - anime
print(fav_hobbies)
step_by_two = hobbies[::2]
print(step_by_two)
# reversing a list with slicing
reversed_hobbies = hobbies[::-1]
print(reversed_hobbies)
# start from the beginning and stop at index 5
print(hobbies[:5])


# what happens if we try to access an index that doesn't exist in the list
print(hobbies[9]) # IndexError because 9 is not a position in our hobbies list


# GET LOOPY

# looping through a list of ice cream flavors
#             0            1            2          3             4               5
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "pistachio"]
# for keyword iterator variable in keyword thing we're iterating through
for flavor in flavors:
    print(flavor)

for flavor in flavors:
    print(f"Oh boy do i sure love sampling {flavor} ice cream")

# using the range function to loop
# range(start, stop, step)
print(range(6))
for i in range(6):
    print(i)

# looping by index using range
#             0            1            2          3             4               5
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "pistachio"]
for i in range(6): # 6 being the length of our flavors list
    print(flavors[i]) # flavors[0] flavors[1] falvors[2]...

# using range(len(list)) to get the indexes for a specific list with an unknown length
for i in range(len(flavors)):
    print(i, flavors[i])

x, y = 1, 2 

# looping with enumerate(our_list)
for i, flavor in enumerate(flavors):
    print(i, flavor) # [(0, "vanilla"), (1, "chocolate")...]

# ============= DOUBLE FOR LOOPS for the DOUBLE SCOOP ===================
#             0            1            2          3             4               5
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "blueberry", "pistachio"]
toppings = ["sprinkles", "chocolate syrup", "whipped cream", "cherry"]
for flavor in flavors:
    for topping in toppings:
        print(f"Lets try a scoop of {flavor} with some {topping} on top")

# break stops loops from running
for flavor in flavors:
    print(flavor)
    if flavor == "chocolate":        
        print("Oh yummy! Thats my favorite! No need to keep looking for ice cream")
        break


# continue to skip over an iteration
for flavor in flavors:
    if flavor == "blueberry":                    
        continue #skip over blueberry
        
    print(flavor)
print(flavors)

# pass creates a placeholder until we figure out what to do with that code block
flavors = ["vanilla", "chocolate", "blueberry", "coffee", "chocolate chip", "blueberry", "pistachio"]
for flavor in flavors:
    if flavor == "coffee":
        pass # ill figure this out later
    print(flavor)


# Looping through multiple lists of the same length by index
#                 0       1        2         3
booth_types = ["Food", "Games", "Music", "Crafts"]
#                    0           1        2         3
schedule_times = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
#                 0          1              2           3
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time}, Item Needed: {item}")

#               0           1           2
flavors = ["chocolate", "vanilla", "strawberry"]
#             0             1             2
toppings = ["sprinkles", "cherry", "chocolate syrup"] 

for i in range(len(flavors)):
    print(i)
    ice_cream = flavors[i]
    topping = toppings[i]
    print(f"On my {ice_cream} ice cream i like {topping}")

# .count() and sum()
# how to do both with for loop
item_prices = [2.99, 5.49, 3.25, 13.99, 4.75]
# using sum to calculate the total price
print((sum(item_prices)/len(item_prices))) # average item price

# getting a sum with a for loop
item_total = 0 # counter variable, but we're continuously add to this for each item in our item_prices
for price in item_prices:
    item_total += price
print(f"Thank your for shopping at Aldi! Your total is {item_total}")
print(item_total/len(item_prices))

# working with lists in lists with loops
inventory = [
    ["Apples", 5],
    ["Bananas", 2],
    ["Oranges", 0],
    ["Milk", 1],
    ["Eggs", 12]
]

print(inventory[1][1])
reorder_threshold = 3


# check each item (which is a list with two items) and see what needs to be reordered
for item in inventory:
    name, quantity = item #["item", integer quantity]
    if quantity < reorder_threshold:
        print(f"{name} needs to be reordered")
    else:
        print(f"We have a lot of {name} in stock")


# ===================== WONDERFUL WORLD OF WHILE LOOPS =============================
# syntax for while loop
# while condition_is_true:
    # do somethign here until that conidtion is no longer true

# variable that we're checking is less than 5
marshmallows = 0
# setting the condition for the while loop to run
while marshmallows < 5:
# we add 1 to marshmallows variable for each iteration
    marshmallows += 1
    print(marshmallows)
    # eventually marshmallows increments over 5 and the while loop breaks
    

# be careful with our conditions
# if our condition is never true our while loop will never run
marshmallows = 0
# setting the condition for the while loop to run
while marshmallows > 5: # wont run because it will never be true with the current variable
# we add 1 to marshmallows variable for each iteration
    marshmallows += 1
    print(marshmallows)
    # eventually marshmallows increments over 5 and the while loop breaks

# being careful that our condition is always true


# marshmallows = 0
# while marshmallows < 5: 
#     marshmallows -= 1
#     print(marshmallows)

# in the above the while loop will never stop running
# because we're decrementing our counter and it will never be greater than 5

# using user input with a while loop
# break when the user says quit
# while True:
#     user_input = input("Say 'stop' to end the refill")
#     if user_input.lower() == 'stop': #.lower() is a string method that changes all characters to lower case
#         print("Enjoy your coffee")
#         break
#     else:
#         print("Heres more coffee")


# adding items to a shopping cart
# cart = []
# print("Hi welcome to Aldi, what can i help you with today?")
# while True:
#     user_input = input("Tell us what you'd like to add to your cart or say 'quit' to quit: ")
#     if user_input == "quit":
#         print("Thanks for shopping here are your items: ")
#         for item in cart:
#             print(item)
#         break
#     else:
#         cart.append(user_input)
#         print(f"Your cart so far {cart}")



# to do list
# to_do_list = []

# def add_item(to_do_list):
#     item = input("What do you need to do? ")
#     to_do_list.append(item)
# while True:
#     choice = input("What would you like to do? add/remove/view/mark as complete")
#     if choice == "add":
#         add_item()
#     elif choice == "remove":
#         remove_item()

import random
names = ["Kayla", "Victor", "Chris", "Karen", "Winter"]
# random.choice() gives us a random item from an iterable
print(random.choice(names))

# randint gives a random number from a range of numbers
# roll some dice
for num in range(10):
    print(num)
    dice_roll = random.randint(1,20) #includes both the 1 and the 20
    print(f"You rolled a {dice_roll}!")

# random.shuffle shuffle a list of stuff
playlist = ["N95", "Careless Whipser", "21 Gun Salute", "Whats Up"]
random.shuffle(playlist)
for song in playlist:
    print(song)

# random.choice with a while loop
snacks = ["peanut butter cups", "fruit snacks", "carrot stick", "chocolate bar"]
# picked_snack = ''
while picked_snack != 'chocolate bar':
    picked_snack = random.choice(snacks)
    print(f"You got a {picked_snack}")
    if picked_snack != "chocolate bar":
        print("lets pick again!")
    else:
        print("Yay chocolate")


# while True:
#     picked_snack = random.choice(snacks)
#     print(f"You got a {picked_snack}")
#     break
#     if picked_snack != "chocolate bar":
#         print("lets pick again!")
#     else:
#         print("Yay chocolate")
#         break





