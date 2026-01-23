def write_zander():
    kichco = float(input("The length of the zander (cm): "))
    gioihan = 42

    if kichco < gioihan:
        print("Release fish back.")
        print(f"Because fish {gioihan - kichco:.1f} cm below the limit.")
    else:
        print("The zander meets the size limit.")
write_zander()