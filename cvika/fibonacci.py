def pamataj(funkcia):
    data = {}
    
    def obalovac(n):
        if n not in data:
            data[n] = funkcia(n)
        return data[n]
        
    return obalovac

@pamataj
def fibonacci(n):
    global pocitadlo
    pocitadlo = pocitadlo + 1
    print(f'{pocitadlo} - pocitam {n}')
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

pocitadlo = 0
print(fibonacci(10))