def facto (sayi):
    if sayi == 0:
        return 1
    else:
        return sayi * facto(sayi-1)
    

sayi = int (input("faktöriyelini hesaplamak istediğiniz sayıyı giriniz:"))

print(f"{sayi}! = {facto (sayi)}")
print(f"{sayi}N = {facto (sayi)}")