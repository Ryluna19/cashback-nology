from cashback import calculate_cashback

cashback_1 = calculate_cashback("vip", 600, 20)
cashback_2 = calculate_cashback("normal", 600, 10)
cashback_3 = calculate_cashback("vip", 600, 15)

print("Questão 2:", cashback_1)
print("Questão 3:", cashback_2)
print("Questão 4:", cashback_3)