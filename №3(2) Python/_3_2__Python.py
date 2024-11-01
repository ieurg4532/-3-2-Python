b = str(input("Введіть слово: "))
if any(char.isdigit() for char in b):
    print("В рядку є цифри")
else:
    print("В рядку немає цифр")

