import sys

try:
    print(f"podil je: {int(sys.argv[1])/int(sys.argv[2])}")
except IndexError:
    print("Zadej dva parametry na příkazovou řádku!")
#except ValueError:
    #print("Zadej čísla jako parametry na příkazovou řádku!")
except ZeroDivisionError:
    print("Zadej druhy parametr ruzny od nuly!")