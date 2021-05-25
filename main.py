import random
from linkedlist import LinkedList
from binary_search_tree import TreeNode
from binary_search_tree import Tree

# Months of Year

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

for index in months:
    if index == "March":
        print("\n\n")
        print(index)
        print("\n\n")
        break


# Birthday Locations

birthday_locations = ["Florida", "North Carolina", "Tennessee"]
birthday_locations.extend(("Mars", "The Moon", "Mexico"))

for index in birthday_locations:
    print(index)


# Sweepstakes Contestants

contestants = [
    {
        "first_name": "Larry",
        "last_name": "Lobster",
        "id": 1
    },
    {
        "first_name": "Will",
        "last_name": "Forte",
        "id": 2
    },
    {
        "first_name": "Joan",
        "last_name": "Rivers",
        "id": 3
    },
    {
        "first_name": "Bill",
        "last_name": "Paxton",
        "id": 4
    },
    {
        "first_name": "Jackie",
        "last_name": "Chan",
        "id": 5
    }
]


def draw_winner():
    print("\n\n")
    i = random.randint(0, len(contestants) -1)
    winner_first_name = contestants[i]["first_name"]
    winner_last_name = contestants[i]["last_name"]
    print(f"Congratulations to our winner {winner_first_name} {winner_last_name}!!!")


draw_winner()

# Family List

family = [
    {
        "first_name": "Paul",
        "last_name": "Bunyon",
        "relationship": "Father"
    },
    {
        "first_name": "Martha",
        "last_name": "Stewart",
        "relationship": "Mother"
    },
    {
        "first_name": "Jim",
        "last_name": "Jones",
        "relationship": "Brother"
    },
    {
        "first_name": "Jamie",
        "last_name": "Farr",
        "relationship": "Brother"
    }
]


# Linked list

print("\n\n Linked list test below:\n")

linked_list = LinkedList()
linked_list.append_node(55)
linked_list.append_node(60)
linked_list.append_node(65)

print(linked_list.head.data)
print(linked_list.tail.data)

linked_list.add_to_beginning(10)  # <----Function for adding to beginning

print(linked_list.head.data)
print(linked_list.tail.data)

linked_list.contains(60)          # <----Function to see if list contains specific node
linked_list.contains(40000)


# Binary search tree

print("\n\n Binary search tree test below:\n")

search_tree = Tree()

search_tree.insert(40)
search_tree.insert(87)
search_tree.insert(42)
search_tree.insert(80)

search_tree.find(80)
search_tree.find(0)
