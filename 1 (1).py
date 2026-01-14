#cau 1
ten = input("Enter your name: ")
print(f"Hello, {ten}!")

#cau 2
import math
bk = float(input("nhap duong kinh hinh tron: "))
cv = 2 * math.pi * bk
print("chu vi hinh tron la :", cv)

#cau 3
dai = float(input("nhap chieu dai: "))
rong = float(input("nhap chieu rong: "))

chuvi = 2 * (dai + rong)
dientich = dai * rong

print("chu vi:", chuvi)
print("dien tich:", dientich)

#cau 4
so_1 = int(input("nhap so 1: "))
so_2 = int(input("nhap so 2: "))
so_3 = int(input("nhap so 3: "))

tong = so_1 + so_2 + so_3
tich = so_1 * so_2 * so_3
tb = tong / 3

print("tong:", tong)
print("tich:", tich)
print("trung binh cua 3 so:", tb)

#cau 5
talents = float(input("nhap talents: "))
pounds = float(input("nhap  pounds: "))
lots = float(input("nhap lots: "))
grams = (
    talents * 20 * 32 * 13.3 +
    pounds * 32 * 13.3 +
    lots * 13.3
)
kilograms = int(grams // 1000)
gram_con_lai = grams % 1000
print("The weight in modern units:")
print(f"{kilograms} kilograms and {gram_con_lai:.2f} grams")

#cau 6
import random
code_3 = [random.randint(0, 9) for _ in range(3)]
code_4 = [random.randint(1, 6) for _ in range(4)]
print("3-digit code:", code_3)
print("4-digit code:", code_4)