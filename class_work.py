print('how many kilometers did you cycle today?')

kms = input() # get user input

miles = float(kms)/1.60934 # converting from string to float and divide

miles = round(miles, 2) # Round the result

print(f"Your{kms}km ride was{miles}ml")

