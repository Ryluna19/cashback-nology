import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from cashback import calculate_cashback
from database import save_query, get_history_by_ip

app = Flask(__name__)
CORS(app)


def get_user_ip():
    # Pega o IP do usuário
    forwarded_ip = request.headers.get("X-Forwarded-For")

    if forwarded_ip:
        return forwarded_ip.split(",")[0].strip()

    return request.remote_addr


def format_history(history):
    # Formata os dados do banco para JSON
    formatted_history = []

    for item in history:
        formatted_history.append({
            "customer_type": item["customer_type"],
            "purchase_value": float(item["purchase_value"]),
            "discount_percentage": float(item["discount_percentage"]),
            "cashback": float(item["cashback"]),
            "created_at": item["created_at"].strftime("%Y-%m-%d %H:%M:%S")
        })

    return formatted_history


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "message": "API em execução"
    })


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "O corpo da requisição é obrigatório."
        }), 400

    customer_type = data.get("customer_type")
    purchase_value = data.get("purchase_value")
    discount_percentage = data.get("discount_percentage", 0)

    if not customer_type or purchase_value is None:
        return jsonify({
            "error": "Tipo de cliente e valor da compra são obrigatórios."
        }), 400

    customer_type = customer_type.lower()

    if customer_type not in ["normal", "vip"]:
        return jsonify({
            "error": "O tipo de cliente deve ser normal ou vip."
        }), 400

    try:
        purchase_value = float(purchase_value)
        discount_percentage = float(discount_percentage)
    except ValueError:
        return jsonify({
            "error": "Valor da compra e desconto devem ser números."
        }), 400

    if purchase_value <= 0:
        return jsonify({
            "error": "O valor da compra deve ser maior que zero."
        }), 400

    if discount_percentage < 0 or discount_percentage > 100:
        return jsonify({
            "error": "O desconto deve estar entre 0 e 100."
        }), 400

    cashback = calculate_cashback(
        customer_type,
        purchase_value,
        discount_percentage
    )

    user_ip = get_user_ip()

    save_query(
        user_ip,
        customer_type,
        purchase_value,
        discount_percentage,
        cashback
    )

    return jsonify({
        "customer_type": customer_type,
        "purchase_value": purchase_value,
        "discount_percentage": discount_percentage,
        "cashback": cashback
    })


@app.route("/history", methods=["GET"])
def history():
    user_ip = get_user_ip()

    history = get_history_by_ip(user_ip)

    return jsonify({
        "user_ip": user_ip,
        "history": format_history(history)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)