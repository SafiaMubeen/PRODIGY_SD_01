def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

value = float(input("Enter the temperature value: "))
unit = input("Enter the unit of temperature (Celsius, Fahrenheit, Kelvin): ").lower()

if unit == "celsius":
    print(f"{value} degrees Celsius is {celsius_to_fahrenheit(value)} degrees Fahrenheit and {celsius_to_kelvin(value)} Kelvin.")
elif unit == "fahrenheit":
    print(f"{value} degrees Fahrenheit is {fahrenheit_to_celsius(value)} degrees Celsius and {fahrenheit_to_kelvin(value)} Kelvin.")
elif unit == "kelvin":
    print(f"{value} Kelvin is {kelvin_to_celsius(value)} degrees Celsius and {kelvin_to_fahrenheit(value)} degrees Fahrenheit.")
else:
    print("Unknown unit of temperature.")