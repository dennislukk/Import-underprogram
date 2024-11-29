import utakning

def main():
    """Samler systeminformasjon og lagrer den i en fil."""
    info = utakning.funk_get_system_info()
    utakning.funk_save_info_to_file(info)

if __name__ == "__main__":
    main()

    
obj_FillInn = open("DESKTOP-ENM4RF4_info.txt", "r")

print(obj_FillInn.read())

obj_FillInn.close()
