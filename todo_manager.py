# todo_manager.py - simple interactive to-do list

print("=" * 40)
print("My To-Do List".center(40))
print("=" * 40)

# /List/ of things to do
to_do_text = ["Morning pilates-5:45", "Study-8:00", "Buy shoes for hike"]

# Display tasks
for to_do in range(len(to_do_text)):
    print(f"{to_do_text[to_do]}")

print(f"\nTotal tasks: {len(to_do_text)}")
print("-" * 40)

# Task list management - adding/removing tasks
print("\nWould you like to:\n1 - Add a task\n2 - Remove a task ")

try:
    choice = int(input("Choice: "))  
    choice1 = 1
    choice2 = 2 

    if choice == choice1: #adding a task
        choice1 = input("Enter new task: ")
        print("\nNew task added")
        to_do_text.append(choice1)

    if choice == choice2: #removing a task
        choice2 = int(input("Enter task to be removed: "))
        print("\nTask removed")
        to_do_text.pop(choice2 - 1)

    print("=" * 40)
    print("Updated To-DO List".center(40))
    print("=" * 40)

except ValueError, IndexError:
    print("Error. Please enter enter a valid number ")
    exit()

# Displaying updated list
for to_do in range(len(to_do_text)):
    print(f"{to_do_text[to_do]}")

print("-" * 40)
print(f"Total tasks: {len(to_do_text)}")