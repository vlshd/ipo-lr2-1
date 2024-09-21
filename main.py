n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples_kazdomy = k // n
apples_ostanetsa = k % n
print(f"Каждому школьнику достанется {apples_kazdomy} яблок(а).")
print(f"В корзинке останется {apples_ostanetsa} яблок(а).")