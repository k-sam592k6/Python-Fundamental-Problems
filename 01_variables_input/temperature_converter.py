def celcius_to_fareheit(c):
    
    cfar = (c * (9/5)) + 32
    print("Fareheit:", cfar)

def celcius_to_kelvin(c):

    ckel = c + 273.15
    print("Kelvin:", ckel)

def kelvin_to_fareheit(k):
    kelc1 = k - 273.15
    print("Fareheit:", celcius_to_fareheit(kelc1))

def kelvin_to_celcius(k):

    kelc2 = k - 273.15
    print("Celcius:", kelc2)

def fareheit_to_celcius(f):
    
    farc = (f - 32)* (9/5)
    print("Celcius:", farc)

def fareheit_to_kelvin(f):
    a = fareheit_to_celcius(f)
    print("Kelvin:", celcius_to_kelvin(a))

value = float(input("Enter Temprature Value:"))
unit = str(input("Enter Unit (C/F/K:)"))

if unit == "C" or unit == "c":
    print("Celcius:", unit,"°C")
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

