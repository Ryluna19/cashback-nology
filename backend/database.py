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
        database=os.getenv("DB_NAME"),
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

    values = (user_ip, customer_type, purchase_value, discount_percentage, cashback)

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
            id,
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
def delete_query_by_id_and_ip(query_id, user_ip):
    # Deleta uma consulta apenas se ela pertencer ao IP do usuário
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        DELETE FROM tbl_cashback_queries
        WHERE id = %s AND user_ip = %s
    """

    cursor.execute(sql, (query_id, user_ip))
    connection.commit()

    deleted_rows = cursor.rowcount

    cursor.close()
    connection.close()

    return deleted_rows > 0
    
    

   
