def citaj_data(subor):
    pass


def zapis_data(subor, data):
    pass


def zozipsuj(subor1_in, subor2_in, subor_out):
    data1 = citaj_data(subor1_in)
    data2 = citaj_data(subor2_in)

    data_out = data1 + data2
    data_out.sort()

    zapis_data(subor_out, data_out)
