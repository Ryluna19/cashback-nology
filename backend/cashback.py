def calculate_cashback(customer_type, purchase_value, discount_percentage):
    discount_value = purchase_value * discount_percentage / 100
    final_purchase_value = purchase_value - discount_value

    base_cashback = final_purchase_value * 0.05
    final_cashback = base_cashback

    # Bônus VIP: 10% sobre o cashback base
    if customer_type.lower() == "vip":
        vip_bonus = base_cashback * 0.10
        final_cashback += vip_bonus

    # Promoção: compras acima de R$ 500 recebem cashback em dobro
    if final_purchase_value > 500:
        final_cashback *= 2

    return round(final_cashback, 2)