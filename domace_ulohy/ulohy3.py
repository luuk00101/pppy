import itertools


def translate_to_pig_latin(word):
    if word[0].lower() in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


def velkosti_akvaria(velkost):
    import itertools

    kombinacie = itertools.permutations(range(velkost + 1), 3)

    for kombinacia in kombinacie:
        sucin = 1

        for cislo in kombinacia:
            sucin *= cislo

        if sucin == velkost:
            yield kombinacia


def stitok(informacia):
    if isinstance(informacia, list):
        velkost, sprava = informacia
    else:
        velkost = informacia
        sprava = ""

    match velkost:
        case "s" | "small" | "malá":
            velkost_text = "malá veľkosť"
        case "m" | "medium" | "stredná":
            velkost_text = "stredná veľkosť"
        case "l" | "large" | "veľká":
            velkost_text = "veľká veľkosť"
        case _:
            velkost_text = "neznáma veľkosť"

    if sprava:
        return f"{velkost_text}: {sprava}"
    else:
        return velkost_text


for kombinacia in velkosti_akvaria(10):
    print(kombinacia)
