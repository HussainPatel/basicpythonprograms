# Write a Python program to convert kilometers to miles.
kiloMeter = float(input("Enter distance in Kilometer: "))
# Conversion factor : 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kiloMeter * conversion_factor
print(F" the distance in Miles is : {miles}")