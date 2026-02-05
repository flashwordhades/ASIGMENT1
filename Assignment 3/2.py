while True:
    inches = float(input("put inches (negative value to end): "))
    if inches < 0:
        print("the program ends.")
        break
    
    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters} cm")
