# simple store receipt simulation
# product information (often arrives as strings from files or user input)


item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = 0.075 #7.5% sales tax

# convert string values to appropriate types for calculations
notebook_price = float(item1_price)
notebook_qty = int(item1_qty)

pen_pack_price = float(item2_price)
pen_pack_qty = int(item2_qty)

backpack_price = float(item3_price)
backpack_qty = int(item3_qty)

# calculation for each item's line total
notebook_total = notebook_price * notebook_qty
pen_pack_total = pen_pack_price * pen_pack_qty
backpack_total = backpack_price * backpack_qty

# calculate subtotal, tax, and total
subtotal = notebook_total + pen_pack_total + backpack_total
tax = subtotal * tax_rate
total = subtotal + tax

# display the receipt
print("=" * 45) #for aesthetic purposes
print("STORE RECEIPT".center(45))
print("=" * 45)

print(f"Notebook            ${notebook_price} x {notebook_qty}      {notebook_total}")     
print(f"Pen Pack            ${pen_pack_price} x {pen_pack_qty}       {pen_pack_total:.2f}")
print(f"Backpack            ${backpack_price} x {backpack_qty}     {backpack_total}")

print("-" * 45) # for aesthetic purposes 

print(f"Subtotal:                          ${subtotal}")
print(f"Tax (7.5%):                        ${tax:.2f}")

print(f"=" * 45) # for aesthetic purposes

print(f"TOTAL:                             ${total:.2f}")

print("=" * 45) # for aesthetic purposes 
