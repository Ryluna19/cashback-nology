CREATE TABLE IF NOT EXISTS tbl_cashback_queries (
    id SERIAL PRIMARY KEY,
    user_ip VARCHAR(45) NOT NULL,
    customer_type VARCHAR(20) NOT NULL,
    purchase_value NUMERIC(10,2) NOT NULL,
    discount_percentage NUMERIC(5,2) NOT NULL,
    cashback NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);