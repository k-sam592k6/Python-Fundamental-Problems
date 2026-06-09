def celcius_to_fareheit(c):
    
    return (c * (9/5)) + 32

def celcius_to_kelvin(c):
    return c + 273.15

def kelvin_to_fareheit(k):
    return k - 273.15
    
def kelvin_to_celcius(k):

    return k - 273.15
    

def fareheit_to_celcius(f):
    
    return (f - 32)* (5/9)
    
def fareheit_to_kelvin(f):
    a = fareheit_to_celcius(f)
    return celcius_to_kelvin(a)

value = float(input("Enter Temprature Value:"))
unit = str(input("Enter Unit (C/F/K:)"))

if unit == "C" or unit == "c":
    print("Celcius:", value,"°C")
    print("Fareheit:", celcius_to_fareheit(value),"°F")
    print("Kelvin:", celcius_to_kelvin(value),"K")

elif unit == "F" or unit == "f":
    print("Celcius:", fareheit_to_celcius(value),"°C")
    print("Fareheit:", value,"°F")
    print("Kelvin:", fareheit_to_kelvin(value),"K")

elif unit == "K" or unit == "k":
    print("Celcius:", kelvin_to_celcius(value),"°C")
    print("Fareheit:", kelvin_to_fareheit(value),"°F")
    print("Kelvin:", value,"K")

