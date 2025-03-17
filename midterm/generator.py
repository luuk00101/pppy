def ch_range(arg1, arg2=None, step=None):
    if step == 0:
        raise ValueError
    if arg2 != None and step != None and ord(arg2) < ord(arg1) and step > 0:
        raise ValueError

    if arg2 == None:
        i = 0

        while i < ord(arg1):
            yield chr(i)
            i += 1

    elif step == None:
        i = ord(arg1)

        while i < ord(arg2):
            yield chr(i)
            i += 1
    elif ord(arg2) < ord(arg1):

        i = ord(arg1)

        while i > ord(arg1):
            yield chr(i)
            i += step

    else:
        i = ord(arg1)

        while i < ord(arg2):
            yield chr(i)
            i += step
