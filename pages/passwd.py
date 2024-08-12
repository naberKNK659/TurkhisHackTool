import random

def passwd():
    max = 2000000
    min = 6

    Passwdlen = int(input("Şifre Uzunluğu: "))

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&()*+,-./:;<=>?@[]^_`{|}~'

    def uzunluk_ctl(girdi):
        if min <= girdi <= max:
            GuncelPasswd = [random.choice(chars) for _ in range(girdi)]
            return ''.join(GuncelPasswd)
        else:
            return "En az {} olmalıdır. En fazla {} olmalıdır. Tekrar deneyiniz.".format(min, max)

    try:
        Passwdlen = int(Passwdlen)
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        exit()

    sonuc = uzunluk_ctl(Passwdlen)
    print("Şifre: " + sonuc)