CREATE DATABASE IF NOT EXISTS db_cashback_nology;

USE db_cashback_nology;

CREATE TABLE IF NOT EXISTS tbl_cashback_queries (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_ip VARCHAR(45) NOT NULL,
    customer_type VARCHAR(20) NOT NULL,
    purchase_value DECIMAL(10,2) NOT NULL,
    discount_percentage DECIMAL(5,2) NOT NULL,
    cashback DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB;