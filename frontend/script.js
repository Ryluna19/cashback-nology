const API_URL = "https://cashback-nology-532z.onrender.com";

const form = document.getElementById("cashbackForm");
const result = document.getElementById("result");
const historyList = document.getElementById("historyList");

function formatCurrency(value) {
    return value.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });
}
function formatDate(dateValue) {
    const date = new Date(dateValue);

    return date.toLocaleString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    });
}
function formatCustomerType(customerType) {
    if (customerType === "vip") {
        return "VIP";
    }

    return "Normal";
}

async function calculateCashback(event) {
    event.preventDefault();

    const customerType = document.getElementById("customerType").value;
    const purchaseValue = document.getElementById("purchaseValue").value;
    const discountPercentage = document.getElementById("discountPercentage").value;

    const response = await fetch(`${API_URL}/calculate`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            customer_type: customerType,
            purchase_value: Number(purchaseValue),
            discount_percentage: Number(discountPercentage)
        })
    });

    const data = await response.json();

    if (!response.ok) {
        result.classList.remove("hidden");
        result.innerHTML = `<strong>Erro:</strong> ${data.error}`;
        return;
    }

    result.classList.remove("hidden");
    result.innerHTML = `
        <strong>Cashback calculado:</strong> ${formatCurrency(data.cashback)}
    `;

    loadHistory();
}

async function loadHistory() {
    const response = await fetch(`${API_URL}/history`);
    const data = await response.json();

    historyList.innerHTML = "";

    if (data.history.length === 0) {
        historyList.innerHTML = "<p>Nenhuma consulta encontrada.</p>";
        return;
    }

    data.history.forEach((item) => {
        const historyItem = document.createElement("div");
        historyItem.classList.add("history-item");

        historyItem.innerHTML = `
            <p><strong>Cliente:</strong> ${formatCustomerType(item.customer_type)}</p>
            <p><strong>Valor da compra:</strong> ${formatCurrency(item.purchase_value)}</p>
            <p><strong>Desconto:</strong> ${item.discount_percentage}%</p>
            <p><strong>Cashback:</strong> ${formatCurrency(item.cashback)}</p>
            <p><strong>Data:</strong> ${formatDate(item.created_at)}</p>

            <button class="delete-button" onclick="deleteHistoryItem(${item.id})">
                Deletar
            </button>
          `;

        historyList.appendChild(historyItem);
    });
}

async function deleteHistoryItem(id) {
    const confirmDelete = confirm("Deseja deletar este registro do histórico?");

    if (!confirmDelete) {
        return;
    }

    const response = await fetch(`${API_URL}/history/${id}`, {
        method: "DELETE"
    });

    const data = await response.json();

    if (!response.ok) {
        alert(data.error);
        return;
    }

    loadHistory();
}

form.addEventListener("submit", calculateCashback);

loadHistory();