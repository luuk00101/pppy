def funkcia(par, *args, **kwargs):
    print(par)
    for hodnota in args:
        print(hodnota)
    for kluc, hodnota in kwargs.items():
        print(kluc, hodnota)


funkcia("test", 1, 2, 3, a=4, b=5, c=6)
