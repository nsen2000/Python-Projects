print ("Welcome to tip calculator")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

total_float = float(total)
total_float = total_float * (1 + (int(tip) / 100))
total_float = total_float / int(split)
print(f"Each person should pay: ${round(total_float, 2)}")

k = input("press anything to exit")