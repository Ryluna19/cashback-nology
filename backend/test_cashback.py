from cashback import calculate_cashback


def test_vip_purchase_with_20_percent_discount():
    assert calculate_cashback("vip", 600, 20) == 26.40


def test_normal_purchase_with_10_percent_discount():
    assert calculate_cashback("normal", 600, 10) == 54.00


def test_vip_purchase_with_15_percent_discount():
    assert calculate_cashback("vip", 600, 15) == 56.10