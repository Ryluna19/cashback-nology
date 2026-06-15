def calculate_cashback(customer_type, purchase_value, discount_percentage):
    # Calcula o valor do desconto
    discount_value = purchase_value * discount_percentage / 100

    # Calcula o valor final da compra
    final_purchase_value = purchase_value - discount_value

    # Cashback base de 5%
    base_cashback = final_purchase_value * 0.05

    # Promoção: compras acima de 500 ganham cashback em dobro
    if final_purchase_value > 500:
        base_cashback = base_cashback * 2

    # Bônus VIP: 10% sobre o cashback base
    if customer_type.lower() == "vip":
        vip_bonus = base_cashback * 0.10
    else:
        vip_bonus = 0

    # Cashback final
    final_cashback = base_cashback + vip_bonus

    return round(final_cashback, 2)