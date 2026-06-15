from database import save_query, get_history_by_ip

test_ip = "127.0.0.1"

save_query(
    test_ip,
    "vip",
    600,
    20,
    26.40
)

history = get_history_by_ip(test_ip)

print(history)