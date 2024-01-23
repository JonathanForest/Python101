"""

Fix this program!

When you run this the first time, there will be a bunch of syntax errors you will need to solve.

After that, you will find that the program doesn't work quite as intended...

It is meant to be a small program that acts as a shopping list. You should be able to;

    - View the list
    - Add items to the list
    - Remove items from your list
    - Check if an item is in the list
    - Clear the list


"""


def display_menu():
    print("\nShopping List Menu:")
    print("1. View List"
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Check if Item is in List")
    print("5. Clear List")
    print("6. Exit"

def view_list(shopping_list)
    print("\nShopping List:")
    for index, item in enumerate(shopping_list, start=1)
        print(f"{index}. {item}")

def add_item(shopping_list)
    item = input("Enter the item to add: "
    shopping_list = shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_item(shopping_list):
    view_list(shopping_list)
    try:
        index = int(input("Enter the index of the item to remove: "))
        removed_item = shopping_list.pop(index)
        print(f"{removed_item} has been removed from the list.")
    except ValueError, IndexError:
        print("Invalid index. Please enter a valid index from the list."

def check_item(shopping_list):
    item_to_check = input("Enter the item to check: "
    if item_to_check in shopping_list:
        print(f"{item_to_check} is in the list.")
    if not item_to_check in shopping_list:
        print(f"{item_to_check} is not in the list."

def clear_list(shopping_list):
    shopping_list.clear()
    print("Shopping list has been cleared."

def main():
    shopping_list = []

    while True
        display_menu()
        choice = input("Enter your choice (1-6): "

        if choice = "1":
            view_list(shopping_list)
        elif choice == "2"
            add_item(shopping_list)
        elif choice == 3:
            remove_item(shopping_list)
        elif choice == "4"
            clear_list(shopping_list)
        elif choice == "5":
            check_item(shopping_list)
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6."


if __name__ == "__main__":
    # Hint, main is a function that needs to be called...
    main
