import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    # Cria conexão com o banco de dados
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


def save_query(user_ip, customer_type, purchase_value, discount_percentage, cashback):
    # Salva uma consulta de cashback no banco
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO tbl_cashback_queries (
            user_ip,
            customer_type,
            purchase_value,
            discount_percentage,
            cashback
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        user_ip,
        customer_type,
        purchase_value,
        discount_percentage,
        cashback
    )

    cursor.execute(sql, values)
    connection.commit()

    cursor.close()
    connection.close()


def get_history_by_ip(user_ip):
    # Busca o histórico de consultas pelo IP do usuário
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = """
        SELECT
            customer_type,
            purchase_value,
            discount_percentage,
            cashback,
            created_at
        FROM tbl_cashback_queries
        WHERE user_ip = %s
        ORDER BY created_at DESC
    """

    cursor.execute(sql, (user_ip,))
    history = cursor.fetchall()

    cursor.close()
    connection.close()

    return history