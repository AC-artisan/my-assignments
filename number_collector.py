
# Crash proof number_collector.py
# Ask user to enter three numbers, one at a time.
try: 
    choice1_number = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number. Using zero (0) instead.")
    choice1_number = 0
try:
    choice2_number = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number. Using zero (0) instead.")
    choice2_number = 0
try:    
    choice3_number = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number. Using zero (0) instead.")
    choice3_number = 0

# Calculations 
user_numbers = choice1_number , choice2_number , choice3_number

number_sum = choice1_number + choice2_number + choice3_number

number_avg = float(choice1_number + choice2_number + choice3_number) / 3

# Display
print("-" * 45)
print("Number Collector".center(45))
print("-" * 45)

print("\n") 

print(f"Your numbers:  {choice1_number}, {choice2_number}, {choice3_number}")
print(f"Sum: {number_sum}")
print(f"Average: {number_avg:.2f}")
