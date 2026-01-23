def hemoglobin_value():
    while True:
        sex = input("The user biological sex (adult male/adult female): ").lower()
        if sex == "adult male" or sex == "adult female":
            break
        else:
            print("Invalid input. Please enter 'adult male' or 'adult female'.")
    while True:
        try:
            hb = float(input("Enter hemoglobin value (g/l): "))
            break
        except ValueError:
            print("Hemoglobin value must be a number.")

    if sex == "adult female":
        if hb < 117:
            print("Hemoglobin value is low.")
        elif hb > 155:
            print("Hemoglobin value is high.")
        else:
            print("Hemoglobin value is normal.")
    else: 
        if hb < 134:
            print("Hemoglobin value is low.")
        elif hb > 167:
            print("Hemoglobin value is high.")
        else:
            print("Hemoglobin value is normal.")
hemoglobin_value()