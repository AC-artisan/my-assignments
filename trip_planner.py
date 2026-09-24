# trip_planner.py - road trip budget planner


#get user input for trip details
destination_text = input("Enter destination: ")
distance_text = float(input("Enter distance (miles): "))
fuel_text = float(input("Enter fuel efficiency (mpg): "))
gas_price_text = float(input("Enter current gas price per gallon: "))
number_of_nights = int(input("Enter total nights stayed at hotel: "))
hotel_cost_text = float(input("Enter hotel cost per night: "))
food_budget_text = float(input("Enter food budget allowance: "))

#calculate user input to get trip details
gallons_needed = distance_text / fuel_text
total_gas_cost = gallons_needed * gas_price_text
total_hotel_cost = number_of_nights * hotel_cost_text
total_food_cost = (number_of_nights + 1) * food_budget_text
grand_total = total_gas_cost + total_hotel_cost + total_food_cost

print("\n") #empty line for spacing

#display formatted trip summary
print(f"{'=' * 3} {'Road Trip Budget Planner'} {'=' * 3}")
print("\n") #empty line for spacing

print(f"{'Destination: '} {destination_text}")
print(f"{'Distance: '} {distance_text:.2f} miles")
print("\n") #empty line for spacing

print(f"{'-' * 10} {'Cost Breakdown'.center(10)} {'-' * 10}")
print(f"{'Gas':<10} {fuel_text}gal @ ${gas_price_text}/gal:      ${total_gas_cost:.2f}")
print(f"{'Hotel':<10} 3 nights @ ${hotel_cost_text:.2f}:        ${total_hotel_cost:.2f}")
print(f"{'Food':<10} {number_of_nights + 1} days @ ${food_budget_text:.2f}:           ${total_food_cost:.2f}")

print("-" * 45)

print(f"{'Estimated Total:                     '} ${grand_total:.2f}")
